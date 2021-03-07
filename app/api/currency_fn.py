from forex_python.converter import CurrencyRates
from typing import Dict


def currency_func(amount: float, from_curr: str, to_curr: str) -> Dict[str, float]:
    """Allow the user to converty currency from one to another."""
    c = CurrencyRates()
    converted_amount = c.convert(from_curr, to_curr, amount)
    return converted_amount