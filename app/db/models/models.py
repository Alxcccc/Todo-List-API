from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    idUsers = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(60))
    
    tasks = relationship("Task", back_populates="user")
    
class Task(Base):
    __tablename__ = 'Tasks'
    idTask = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    description = Column(String(250))
    idUser = Column(Integer, ForeignKey('Users.idUsers'))
    
    user = relationship("User", back_populates="tasks")