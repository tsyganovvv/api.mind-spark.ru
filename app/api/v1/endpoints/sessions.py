from fastapi import APIRouter, Depends, HTTPException, status, responses
from fastapi.responses import JSONResponse

from app.api.dependencies.services import get_session_service
from app.services.session_service import SessionService
from app.domain.schemas.auth_schemas import LoginRequest

router = APIRouter()


@router.post(
    "/", status_code=status.HTTP_200_OK
)
async def login(
    user_data: LoginRequest, service: SessionService = Depends(get_session_service)
):
    try:
        token = await service.login(user_data.email, user_data.password)
        response = JSONResponse(
            content={"message": "Login successful"},
            status_code=status.HTTP_200_OK
        )
        response.headers["X-Auth-Token"] = token
        response.headers["Authorization"] = f"Bearer {token}"
        return response
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
