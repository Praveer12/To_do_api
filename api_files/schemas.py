from pydantic import BaseModel, EmailStr ,field_validator , Field
from typing import Optional
from datetime import datetime
from enum import Enum
import re


class Role(str,Enum):
    user = "user"
    admin = "admin"
    superuser = "superuser"

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$',
        description="Minimum 8 chars, one uppercase, one lowercase, one number"
    )


class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: Role

class Login(BaseModel):
    email: EmailStr
    password: str


class TaskStatus(str, Enum):
    pending =  "pending"
    in_progress =  "In progress"
    completed = "completed"
    Cancelled = "Cancelled"

class TaskPriority(str, Enum):
    high = "high"
    low = "low"
    medium = "medium"
    urgent = "urgent"

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: TaskPriority
    status: TaskStatus
    due_date: datetime

class TaskOut(BaseModel):
    id: int
    title: str
    description : str
    priority: TaskPriority
    due_date: datetime
    status: TaskStatus
    is_deleted: bool
    created_at : datetime




