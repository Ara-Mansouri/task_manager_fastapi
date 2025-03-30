from pydoc import stripid
from pydantic import BaseModel
from  typing import Optional



class TaskBase(BaseModel):
    Name:str
    Priority:str
    Deadline:str
    
class TaskCreated(TaskBase):
    pass

class Task(TaskBase):
    Id:int
    class Config:
        orm_mode:True


