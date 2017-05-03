from src.sentiment_scorer import SentimentScorer
import unittest

class TestSentimentScorer(unittest.TestCase):

    def setUp(self):
        sentiment_weights = {
            "great" : 2,
            "bad" : -2
        } 
        multiplier_weights = {
            "not" : -1,
            "really" : 1.5
        }
        self._sentiment_scorer = SentimentScorer()
        self._sentiment_scorer.initialize(sentiment_weights, multiplier_weights)

    def test_score_sentiment_phrase(self):
        sentiment_blocks = [([], "great")]
        actual = self._sentiment_scorer.score_sentiment(sentiment_blocks)
        expected = 2.0
        self.assertEqual(actual, expected)

    def test_score_sentiment_phrase_single_multiplier(self):
        sentiment_blocks = [(["really"], "great")]
        actual = self._sentiment_scorer.score_sentiment(sentiment_blocks)
        expected = 3.0
        self.assertEqual(actual, expected)

    def test_score_sentiment_phrase_multiple_multipliers(self):
        sentiment_blocks = [(["not", "really"], "great")]
        actual = self._sentiment_scorer.score_sentiment(sentiment_blocks)
        expected = -3.0
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
    
    
    
    