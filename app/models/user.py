from pydantic import BaseModel, EmailStr, constr
from typing import Union

class User(BaseModel):
    name: str
    email: EmailStr
    password: constr(
        min_length=8,
        max_length=20
    )
    
    class Config:
        validate_assignment = True
        
class UserDb(BaseModel):
    name: str
    email: EmailStr
    password: Union[str, bytes]