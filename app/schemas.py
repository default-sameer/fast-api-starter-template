from app.database import Base
from pydantic import BaseModel


class Student(BaseModel):
    full_name: str
    email: str
   
    class Config:
        orm_mode = True