from datetime import datetime
from typing import Optional

from pydantic import EmailStr

from app.domain.schemas import Base


class UserBase(Base):
    email: EmailStr
    username: str
    fullname: Optional[str] = None


class UserCreate(UserBase):
    password: Optional[str]


class UserUpdate(UserBase):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    fullname: Optional[str] = None
    password: Optional[str] = None


class UserUpdateInDB(UserBase):
    email: EmailStr
    username: str
    fullname: str
    hashed_password: str


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    fullname: str

    class Config:
        from_attributes = True
