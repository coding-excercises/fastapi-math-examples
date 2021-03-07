import unittest
from app.api.currency_fn import currency_func


class CurrencyTestSuite(unittest.TestCase):
    """Test the currency function."""

    def test_func_currency_success(self):
        """Test the currency function."""
        result = currency_func(1, 'USD', 'INR')
        self.assertGreaterEqual(result, 70.0)
