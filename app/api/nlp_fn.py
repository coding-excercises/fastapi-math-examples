from typing import Dict
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment_func(input_text: str) -> Dict[str, int]:
    """Give the user the result of sentiment analysis."""
    analyzer = SentimentIntensityAnalyzer()
    nlp = analyzer.polarity_scores(input_text)
    return (nlp)
