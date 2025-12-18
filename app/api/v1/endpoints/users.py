from fastapi import APIRouter, status, Depends, HTTPException
from app.domain.schemas.users import UserCreate, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.user_service import UserService
from app.api.dependencies.services import get_user_service

router = APIRouter()

@router.get('/')
def users():
    return {
        "success" : True
    }

@router.post('/create_user', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    try:
        return await service.create_user(user_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
