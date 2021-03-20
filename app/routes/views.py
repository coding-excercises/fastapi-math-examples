from typing import Dict
from fastapi import APIRouter
from app.api.health_fn import health_func
from app.api.math_fn import add_func
from app.api.currency_fn import currency_func
from ddtrace import tracer
import logging

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=fastapi-math-examples dd.env=dev dd.version=v1 '
          'dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
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


@tracer.wrap()
@router.get("/health/", tags=["health"])
async def health() -> Dict[str, str]:
    """Give the user the health of API."""
    return health_func()


@tracer.wrap()
@router.get("/math/add", tags=["math - add"])
async def math_add(a: int = 0, b: int = 0) -> Dict[str, int]:
    """Give the user the result of a simple addition."""
    log.info("Input for addition: %s %s", a, b)
    return add_func(a, b)


@tracer.wrap()
@router.get("/util/currency", tags=["util - currency"])
async def currency_conv(from_curr: str = 'USD',
        to_curr: str = 'INR', amt: float= 0.0) -> Dict[str, float]:
    """Give the user the result of currency conversion."""
    log.info("Input for currency conversion: %s %s %s", from_curr, to_curr, amt)
    return currency_func(amt, from_curr, to_curr)
