from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import Optional
from datetime import datetime

# class Category(str, Enum):
#     WORK = "work"
#     PERSONAL = "personal"

class User(BaseModel):
    name: str
    password: str

class UserResponse(BaseModel):
    id : int
    name: str
    create_date: datetime
    model_config = ConfigDict(from_attributes=True)

class UserName(BaseModel):
    id: int
    name:str
    model_config = ConfigDict(from_attributes=True)

class Status(str, Enum):
    DONE = "done"
    PROGRESS = "in-progress"

class Task(BaseModel):
    title: str
    description: str
    category: str
    status: Status = Status.PROGRESS
    due_date: Optional[datetime] = None  # User can provide a due date

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id : int
    title: str
    description: str
    category: str
    status: str
    due_date: datetime
    create_date: datetime
    owner_id: int
    owner: UserName
    model_config = ConfigDict(from_attributes=True)

class TaskResponse2(BaseModel):
    id : int
    title: str
    description: str
    category: str
    status: str
    due_date: datetime
    owner_id: int
    update_date: datetime
    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id: Optional[str] = None