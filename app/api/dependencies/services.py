from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.db.session import get_db
from app.services.user_service import UserService


def get_user_service(
        db: AsyncSession = Depends(get_db)
) -> UserService:
    return UserService(db)