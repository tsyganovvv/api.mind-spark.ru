from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean

from app.domain.models import BaseModel


class Token(BaseModel):
    __tablename__ = "tokens"

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    token = Column(String, unique=True, index=True, nullable=False)
    token_type = Column(String, default="refresh")
    expires_at = Column(DateTime, nullable=False)
    is_revoked = Column(Boolean, default=False)