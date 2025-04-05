from sqlalchemy import Column, Integer, String
from .database import Base


class Task(Base):
    
    __tablename__="Tasks"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,index=True)
    priority =Column(String,default="Medium")
    deadline =Column(String,default="No deadline")
    status =Column(String,default="Pending")
    