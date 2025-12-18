from fastapi import APIRouter

from .v1.endpoints import items, users

router = APIRouter()

router.include_router(items.router, prefix="/v1/items", tags=["items"])
router.include_router(users.router, prefix="/v1/users", tags=["users"])
