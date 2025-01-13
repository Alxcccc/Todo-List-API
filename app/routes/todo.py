from fastapi import APIRouter, Depends
from typing import Annotated

from models.user import User
from routes.login import oauth2_scheme


router = APIRouter(prefix="/api")

@router.get('/todos', summary='All tasks', tags=["CRUD todo list"],)
async def get_tasks(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'message': "awo"}