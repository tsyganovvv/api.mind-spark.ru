from datetime import datetime
from typing import Optional

from pydantic import Field

from app.domain.schemas import Base


class TokenSchema(Base):
    acces_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"


class TokenPair(Base):
    access_token: str = Field(..., description="Access token")
    refresh_token: str = Field(..., description="Refresh token")
    token_type: str = Field(default="bearer", description="token type")


class LoginRequest(Base):
    email: str
    password: str


class RefreshRequest(Base):
    refresh_token: str
