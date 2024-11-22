from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()
users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> list[User]:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        user: User,
        username: Annotated[str, Path(max_length=20, min_length=5, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]
) -> User:
    user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=0, description="Enter User ID", example=1)],
        username: Annotated[str, Path(max_length=20, min_length=5, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> User:
    try:
        users[user_id - 1].username = username
        users[user_id - 1].age = age
        return users[user_id - 1]
    except:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=0, description="Enter User ID", example=1)]) -> List[User]:
    try:
        users.pop(user_id - 1)
        return users
    except:
        raise HTTPException(status_code=404, detail='User was not found')
