from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from routes.login import oauth2_scheme
from auth.token import Token
from models.task import Task, TaskUpdate
from db.database import DataBase


router = APIRouter(prefix="/api")

@router.post('/todos', summary='Create Task', tags=["CRUD todo list"])
async def create_task(task: Task, token: Annotated[str, Depends(oauth2_scheme)]):
    token_ins = Token()
    data_token = token_ins.decode_token(token=token)
    db = DataBase()
    result = db.add_task(data_token, task)
    if result == True:
        db.close_session()
        return {"message": "Add Task successfully"}
    db.close_session()
    raise HTTPException(404, detail=result)

@router.get('/todos', summary='Get all tasks', tags=["CRUD todo list"])
async def get_tasks(token: Annotated[str, Depends(oauth2_scheme)]):
    token_ins = Token()
    data_token = token_ins.decode_token(token=token)
    db = DataBase()
    result = db.read_tasks(data_token)
    if isinstance(result, list):
        for task in result:
            task.idUser = data_token
        db.close_session()
        return {"message": result}
    db.close_session()
    raise HTTPException(404, detail=result)

@router.put('/todos/{id_task}', summary='Update task', tags=["CRUD todo list"])
async def update_task(id_task, task_update: TaskUpdate,token: Annotated[str, Depends(oauth2_scheme)]):
    tokens_ins = Token()
    data_token = tokens_ins.decode_token(token=token)
    db = DataBase()
    result = db.update_task(id_task, data_token, task_update)
    if result == True:
        db.close_session()
        return {"message": "Task update succesfully"}
    db.close_session()
    raise HTTPException(404, detail=result)

@router.delete('/todos/{id_task}', summary='Delete task', tags=["CRUD todo list"])
async def delete_task(id_task, token: Annotated[str, Depends(oauth2_scheme)]):
    tokens_ins = Token()
    data_token = tokens_ins.decode_token(token=token)
    db = DataBase()
    result = db.delete_task(id_task, data_token)
    if result == True:
        db.close_session()
        return {"message": "Task delete succesfully"}
    db.close_session()
    raise HTTPException(404, detail=result)
    
