from fastapi import APIRouter, HTTPException

from db.database import DataBase
from models.user import User

router = APIRouter(prefix="/api")

@router.post('/register', summary='register', tags=["register"],)
async def register(user: User):
    db = DataBase()
    result = db.Users.register_user(user)
    if result == True:
        return {"message": "Registered successfully"}
    raise HTTPException(404, detail=result)