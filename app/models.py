from email.policy import default
from sqlalchemy import column,Integer,string
from database import base


class Task(base):
    
    __tablename__="Tasks"
    id=column(Integer,primary_key=True,index=True)
    Name=column(string,index=True)
    priority =column(string,default="Medium")
    Deadline =column(string,default="No deadline")
    Status =column(string,default="Pending")
    