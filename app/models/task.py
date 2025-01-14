from typing import Union

from pydantic import BaseModel


class Task(BaseModel):
    idTask: Union[int, None] = None
    title: str
    description: str
    idUser: Union[int, None] = None

    class Config:
        validate_assignment = True


class TaskUpdate(BaseModel):
    title: Union[str, None] = None
    description: Union[str, None] = None
