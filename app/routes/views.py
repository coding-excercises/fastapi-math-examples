from typing import Dict
from fastapi import APIRouter
from app.api.health_fn import health_func

router = APIRouter()


@router.get("/health/", tags=["health"])
async def health() -> Dict[str, str]:
    """This controller tries to call the fn and return the health of API."""
    return health_func()
