from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, func, ForeignKey
from sqlalchemy.sql.expression import null
from .database import Base
from sqlalchemy.orm import relationship



class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(50), server_default='personal',nullable=False)
    status = Column(String(50), server_default='in-progress',nullable=False)
    due_date = Column(TIMESTAMP, nullable=True)
    create_date = Column(TIMESTAMP,nullable=False, server_default=func.now())
    update_date = Column(TIMESTAMP, nullable=True, onupdate=func.now())
    owner_id= Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)

    owner = relationship("User") 

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name= Column(String(50), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    create_date = Column(TIMESTAMP,nullable=False, server_default=func.now())