from src.sentiment_scorer import SentimentScorer
import unittest

class TestSentimentScorer(unittest.TestCase):

    def setUp(self):
        sentiment_weights = {
            "great" : 2,
            "uncomfortable" : -1,
            "didn't work" : -1,
            "old" : -1, 
            "hard" : -1,
            "bad" : -2
        } 
        multiplier_weights = {
            "not" : -1,
            "really" : 1.5
        }
        self._sentiment_scorer = SentimentScorer()
        self._sentiment_scorer.initialize(sentiment_weights, multiplier_weights)

    def test_xx(self):
        sentiment_blocks = [([], "great")]
        actual = self._sentiment_scorer.score_sentiment(sentiment_blocks)
        expected = 2
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
    
    
    
    