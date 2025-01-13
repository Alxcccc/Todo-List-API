from pydantic import BaseModel, EmailStr, constr

class User(BaseModel):
    name: str
    email: EmailStr
    password: constr(
        min_length=8,
        max_length=20
    )
    
    class Config:
        validate_assignment = True
        