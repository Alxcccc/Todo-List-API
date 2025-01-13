from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta
import os
from dotenv import load_dotenv

from db.database import DataBase
from models.token import Token

load_dotenv()

router = APIRouter(prefix="/api")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

@router.post('/token', summary='get token', tags=["Auth"],)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    db = DataBase()
    result = db.login(form_data.username, form_data.password)
    if isinstance(result, dict):
        # Logica para crear token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        token = Token()
        access_token_jwt = token.create_token(data=result, expires_delta=access_token_expires)
        db.close_session()
        return {"access_token": access_token_jwt, "token_type": "bearer"}
    raise HTTPException(404, detail=result)