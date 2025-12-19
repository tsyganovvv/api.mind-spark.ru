from typing import Optional, List
from datetime import datetime

from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete, select, and_, or_

from app.domain.models.tokens_models import Token
from app.domain.schemas.tokens_schemas import TokenSchema, TokenPair


class TokenRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_id(self, token_id: int) -> Optional[TokenSchema]:
        result = await self.db.execute(select(Token).where(Token.id == token_id))
        return result.scalar_one_or_none()
    
    async def get_by_token(self, token: str) -> Optional[Token]:
        result = await self.db.execute(select(Token).where(Token.token == token))
        return result.scalar_one_or_none()
    
    async def get_valid_token(self, token: str) -> Optional[Token]:
        result = await self.db.execute(select(Token).where(
            and_(
                Token.token == token,
                Token.is_revoked == False,
                Token.expires_at > datetime.now()
            )
        ))
        return result.scalar_one_or_none()
    
    async def get_user_tokens(self, user_id: int) -> List[Token]:
        result = await self.db.execute(select(Token).where(Token.user_id == user_id))
        return list(result.scalars().all())
    
    async def get_activa_user_tokens(self, user_id: int) -> List[Token]:
        result = await self.db.execute(select(Token).where(
            and_(
                Token.user_id == user_id, 
                Token.is_revoked == False,
                Token.expires_at > datetime.now()
            )
        ))
        return list(result.scalars().all())
    
    async def create(self, token_data: Token)

