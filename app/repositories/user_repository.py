from typing import Optional

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.users_models import User
from app.domain.schemas.users_schemas import UserCreate, UserUpdateInDB


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get(self, user_id: int) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_by_email(self, user_email: str) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.email == user_email))
        return result.scalar_one_or_none()
    
    async def get_by_id(self, user_id: int) -> Optional[User]:
        result = await self.db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> list[User]:
        result = await self.db.execute(select(User).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, user_data: UserCreate, hashed_password: str) -> User:
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            fullname=user_data.fullname,
            hashed_password=hashed_password,
        )
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def update(self, user_id: int, user_data: UserUpdateInDB) -> Optional[User]:
        update_data = user_data.model_dump()
        if not update_data:
            return None
        await self.db.execute(
            update(User).where(User.id == user_id).values(**update_data)
        )
        await self.db.commit()
        result = await self.get(user_id)
        return result

    async def delete(self, user_id: int) -> bool:
        await self.db.execute(delete(User).where(User.id == user_id))
        await self.db.commit()
        return True
