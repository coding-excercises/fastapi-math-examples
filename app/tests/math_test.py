import unittest
from app.api.math_fn import add_func


class MathTestSuite(unittest.TestCase):
    """Test the math function."""

    def test_func_add_success(self):
        """Test the addition function."""
        result = add_func(2, 2)
        self.assertEqual(result, 4)
