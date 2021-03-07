from typing import Dict
from fastapi import APIRouter
from app.api.health_fn import health_func
from app.api.math_fn import add_func

router = APIRouter()


@router.get("/", tags=["home"])
async def home() -> Dict[str, str]:
    """Give the user the home API."""
    return "FastAPI Math Examples"

@router.get("/health/", tags=["health"])
async def health() -> Dict[str, str]:
    """Give the user the health of API."""
    return health_func()

@router.get("/math/add", tags=["math - add"])
async def math_add(a: int = 0, b: int = 0) -> Dict[str, int]:
    """Give the user the result of a simple addition"""
    return add_func(a, b)
