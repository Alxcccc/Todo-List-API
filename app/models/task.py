from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    title: str
    description: str
    id_user: int
    
    class Config:
        validate_assignment = True
        