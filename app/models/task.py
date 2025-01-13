from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class Task(BaseModel):
    title: str
    description: str
    
    class Config:
        validate_assignment = True
        