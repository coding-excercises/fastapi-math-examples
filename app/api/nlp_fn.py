from typing import Dict
import aspect_based_sentiment_analysis as absa


def get_aspect_sentiment_func(input_text: str, 
                        input_entity1: str,
                        input_entity2: str) -> Dict[str, str]:
    """Give the user the result of sentiment analysis."""
    recognizer = absa.aux_models.BasicPatternRecognizer()
    nlp = absa.load(pattern_recognizer=recognizer)
    completed_task = nlp(text=input_text,
                        aspects=[input_entity1,input_entity2])
    input_entity1, input_entity2 = completed_task.examples

    return (str(input_entity1.sentiment),
            str(input_entity1.sentiment.value),
            str(input_entity2.sentiment),
            str(input_entity2.sentiment.value))
