from typing import Dict
from fastapi import APIRouter
from app.api.health_fn import health_func
from app.api.math_fn import add_func
from ddtrace import tracer
import logging

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=fastapi-math-examples dd.env=dev dd.version=v1 dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)
log.level = logging.INFO

router = APIRouter()

@tracer.wrap()
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
    """Give the user the result of a simple addition."""
    log.info("Input for addition: %s %s", a, b)
    return add_func(a, b)
