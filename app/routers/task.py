from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session
from slugify import slugify
from typing import Annotated

from app.backend.db_depends import get_db
from app.models import Task
from app.schemas import CreateTask, UpdateTask


router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    return task


@router.post('/create')
async def create_task():
    pass


@router.put('/update')
async def update_task():
    pass


@router.delete('delete')
async def delete_task():
    pass
