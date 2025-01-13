from fastapi import APIRouter, Depends
from typing import Annotated

from models.user import User
from routes.login import oauth2_scheme
from models.token import Token


router = APIRouter(prefix="/api")

@router.get('/todos', summary='Create Task', tags=["CRUD todo list"],)
async def create_task(token: Annotated[str, Depends(oauth2_scheme)]):
    token_ins = Token()
    data_token = token_ins.decode_token(token=token)
    return {'message': data_token}