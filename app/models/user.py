from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    password: constr(
        min_length=8,
        max_length=20
    )
    
    class Config:
        validate_assignment = True
        