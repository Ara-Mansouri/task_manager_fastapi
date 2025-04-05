from email.policy import default
from sqlalchemy import Column, Integer, String
from .database import Base


class Task(Base):
    
    __tablename__="Tasks"
    id=Column(Integer,primary_key=True,index=True)
    Name=Column(String,index=True)
    priority =Column(String,default="Medium")
    Deadline =Column(String,default="No deadline")
    Status =Column(String,default="Pending")
    