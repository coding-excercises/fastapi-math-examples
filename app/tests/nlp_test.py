import unittest
from app.api.nlp_fn import get_sentiment_func


class NLPTestSuite(unittest.TestCase):
    """Test the sentiment function."""

    def test_func_sentiment_success(self):
        """Test the sentiment function."""
        result = get_sentiment_func("Company shares are going up. But, employees are unhappy.")
        self.assertAlmostEqual(result["neg"], 0.301)
        self.assertAlmostEqual(result["pos"], 0.13)
        self.assertAlmostEqual(result["neu"], 0.569)
        self.assertAlmostEqual(result["compound"], -0.4767)
