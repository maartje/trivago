from src.sentiment_analyser import SentimentAnalyzer
from src.sentiment_scorer import SentimentScorer

import unittest

class TestStringMethods(unittest.TestCase):

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
        sentiment_scorer = SentimentScorer()
        self._sentiment_analyser = SentimentAnalyzer(sentiment_scorer)
        self._sentiment_analyser.initialize(sentiment_weights, multiplier_weights)

    def test_score_sentiment_adds_scores_for_matched_phrases(self):
        text = "The location was great, but the bed uncomfortable"
        actual_score = self._sentiment_analyser.score_sentiment(text)
        expected_score = -1 + 2
        self.assertEqual(actual_score, expected_score)

    def test_score_sentiment_adds_scores_for_matched_phrases_with_multiple_words(self):
        text = "It didn't work for us."
        actual_score = self._sentiment_analyser.score_sentiment(text)
        expected_score = -1
        self.assertEqual(actual_score, expected_score)

    def test_score_sentiment_matches_phrases_case_insensitive(self):
        text = "Great, great, GREAT"
        actual_score = self._sentiment_analyser.score_sentiment(text)
        expected_score = 2 + 2 + 2
        self.assertEqual(actual_score, expected_score)

    def test_score_sentiment_not_matches_partial_words(self):
        text = "The room was cold, but it was hardly a problem"
        actual_score = self._sentiment_analyser.score_sentiment(text)
        expected_score = 0
        self.assertEqual(actual_score, expected_score)

    def test_score_sentiment_multiplies_phrase_score_by_preceding_multiplier_scores(self):
        text = "The location was NOT really great, but it was not bad either"
        actual_score = self._sentiment_analyser.score_sentiment(text)
        expected_score = -1 * 1.5 * 2 + -1 * -2;
        self.assertEqual(actual_score, expected_score)

    def test_score_sentiment_multiplies_phrase_score_correctly_when_term_multiple_times(self):
        text = "The location was great, actually it was really great!"
        actual_score = self._sentiment_analyser.score_sentiment(text)
        expected_score = 2 + 1.5 * 2;
        self.assertEqual(actual_score, expected_score)

if __name__ == '__main__':
    unittest.main()