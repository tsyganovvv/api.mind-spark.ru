from pydantic import EmailStr
from datetime import datetime
from typing import Optional
from app.domain.schemas import Base


class UserBase(Base):
    email: EmailStr
    username: str
    fullname: Optional[str] = None

class UserCreateRequest(UserBase):
    password: str

class UserCreateInDB(UserBase):
    hashed_password: str

class UserUpdate(UserBase):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    fullname: Optional[str] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: bool
    updates_at: Optional[datetime] = None

    class Config:
        from_attributes = True

