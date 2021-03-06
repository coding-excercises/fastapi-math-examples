import unittest
from app.api.health_fn import health_func


class HealthTestSuite(unittest.TestCase):
    """Test the health function."""

    def test_func_health(self):
        result = health_func()
        self.assertEqual(result, "ok")
