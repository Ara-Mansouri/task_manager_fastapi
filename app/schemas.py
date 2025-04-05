from pydantic import BaseModel
from typing import Optional 

class TaskBase(BaseModel):
    name: str
    priority: str
    deadline: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
     
    class Config:
        orm_mode = True
