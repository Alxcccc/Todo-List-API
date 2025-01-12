from fastapi import APIRouter
from models.user import User

router = APIRouter(prefix="/api")

@router.get('/{id}/todos', summary='All tasks', tags=["CRUD todo list"],)
async def get_tasks(id: int):
    return {'message': id}