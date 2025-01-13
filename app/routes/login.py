from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated

from db.database import DataBase

router = APIRouter(prefix="/api")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")


@router.post('/token', summary='get token', tags=["Auth"],)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    db = DataBase()
    result = db.login(form_data.username, form_data.password)
    if result == True:
        return {"access_token": result, "token_type": "bearer"}
    raise HTTPException(404, detail=result)