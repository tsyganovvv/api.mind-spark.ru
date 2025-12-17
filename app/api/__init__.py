from fastapi import APIRouter
from .v1.endpoints import items

router = APIRouter()

router.include_router(items.router, prefix="/v1/items", tags=["items"])