from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()
templates = Jinja2Templates(directory='templates')
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except:
        raise HTTPException(status_code=404, detail='User not found')


@app.post('/user/{username}/{age}')
async def create_user(
        user: User,
        username: Annotated[str, Path(max_length=20, min_length=5, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]
) -> User:
    if users:
        user.id = users[-1].id + 1
    else:
        user.id = 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=0, description="Enter User ID", example=1)],
        username: Annotated[str, Path(max_length=20, min_length=5, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i].username = username
            users[i].age = age
        return users[i]
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=0, description="Enter User ID", example=1)]) -> List[User]:
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            return users
    raise HTTPException(status_code=404, detail='User was not found')
