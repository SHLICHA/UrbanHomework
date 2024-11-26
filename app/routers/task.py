from fastapi import APIRouter
from sqlalchemy import Boolean, ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship

from app.backend.db import Base


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users'), nullable=True)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates='tasks')


router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks():
    pass


@router.get('/task_id')
async def task_by_id():
    pass


@router.post('/create')
async def create_task():
    pass


@router.put('/update')
async def update_task():
    pass


@router.delete('delete')
async def delete_task():
    pass
