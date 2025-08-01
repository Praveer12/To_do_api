from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, Column, DateTime, Boolean, Enum
from api_files.database import *
import enum


class Role(str,enum.Enum):
    user = "user"
    admin = "admin"
    superuser = "superuser"

class Users(Base):

    __tablename__  = "users"

    id = Column(Integer, primary_key= True, index=True)
    email = Column(String, nullable = False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default= datetime.now())
    role = Column(Enum(Role), default="user")

    tasks = relationship('Task', back_populates= 'owner')


class TaskStatus(str, enum.Enum):
    pending =  "pending"
    in_progress =  "In progress"
    completed = "completed"
    Cancelled = "Cancelled"


class TaskPriority(str, enum.Enum):
    high = "high"
    low = "low"
    medium = "medium"
    urgent = "urgent"


class tasks(Base):

    __tablename__ = "tasks"
    id = Column(Integer, primary_key = True, index=True)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    priority = Column(Enum(TaskPriority))
    due_date = Column(DateTime, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    owner_id = Column(Integer, ForeignKey("users.id"))
    is_deleted = Column(Boolean, default= False)
    created_at = Column(DateTime, default= datetime.now())

    owner = relationship('Users', back_populates='tasks')