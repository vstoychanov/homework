from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks

@router.get('/task_id')
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

@router.post('/create')
async def create_task(task_data: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user:
        new_task = Task(
            title=task_data.title,
            content=task_data.content,
            priority=task_data.priority,
            completed=task_data.completed,
            slug=slugify(task_data.title + '-' + str(user.id)),
            user_id=user.id
        )
        db.add(new_task)
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

@router.put('/update')
async def update_task(task_data: UpdateTask, task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        db.execute(update(Task).where(Task.id == task_id).values(
            title=task_data.title,
            content=task_data.content,
            priority=task_data.priority,
            completed=task_data.completed
        ))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

@router.delete('/delete')
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deletion is successful!'}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")