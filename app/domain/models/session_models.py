from sqlalchemy import Column, Integer, ForeignKey, String, DateTime

from app.domain.models import BaseModel


class SessionModel(BaseModel):
    __tablename__ = "sessions"

    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), index=True)
    token = Column(String, unique=True, index=True)
    expires_at = Column(DateTime, index=True)