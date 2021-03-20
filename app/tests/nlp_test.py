import unittest
import aspect_based_sentiment_analysis as absa
from app.api.nlp_fn import get_aspect_sentiment_func


class NLPTestSuite(unittest.TestCase):
    """Test the sentiment function."""

    def test_func_sentiment_success(self):
        """Test the sentiment function."""
        result = get_aspect_sentiment_func("Company shares are going up. But, employees are unhappy.",
                                        "Company",
                                        "employees")
        self.assertEqual(result[0], "Sentiment.positive")
        self.assertEqual(result[1], "2")
        self.assertEqual(result[2], "Sentiment.negative")
        self.assertEqual(result[3], "1")
