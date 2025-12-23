import secrets
from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.session_models import SessionModel


class SessionRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_session(
        self, user_id: int, expires_days: int = 3
    )-> Optional[SessionModel]:
        token = secrets.token_urlsafe(32)
        expire_at = datetime.now() + timedelta(days=expires_days)

        session = SessionModel(
            user_id=user_id,
            token = token,
            expires_at=expire_at
        )
        self.db.add(session)
        await self.db.commit()
        await self.db.refresh(session)
        return session

    async def get_session(
        self, session_id: int
    )-> Optional[SessionModel]:
        user = self.db.execute(select(SessionModel).where(SessionModel.id == session_id))
        return user

    async def delete_session(self, session_id: int) -> Optional[SessionModel]:
        session = self.get_session(session_id)
        if session:
            await self.db.delete(session)
            await self.db.commit()
        return session

    async def is_valid(self, session: SessionModel):
        if not session:
            return False
        return datetime.now(timezone=True) < session.expires_at

