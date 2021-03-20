import unittest
from hypothesis import given, strategies as st
from app.api.math_fn import add_func


class MathTestSuite(unittest.TestCase):
    """Test the math function."""

    def test_func_add_success(self):
        """Test the addition function."""
        result = add_func(2, 2)
        self.assertEqual(result, 4)

    @given(st.integers(), st.integers())
    def test_func_add_hypothesis(self, x, y):
        """Test the addition function based on properties."""
        result = add_func(x, y)
        self.assertEqual(result, x + y)
