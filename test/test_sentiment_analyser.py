from src.sentiment_analyser import SentimentAnalyzer
from src.sentiment_scorer import SentimentScorer
import unittest
from unittest.mock import MagicMock

class TestSentimentAnalyser(unittest.TestCase):

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
        self._sentiment_scorer.score_sentiment = MagicMock(return_value = -30)
        self._sentiment_analyser = SentimentAnalyzer(self._sentiment_scorer)
        self._sentiment_analyser.initialize(sentiment_weights, multiplier_weights)

    def test_score_sentiment_adds_scores_for_matched_phrases(self):
        text = "The location was great, but the bed uncomfortable"
        self._sentiment_analyser.score_sentiment(text)
        self._sentiment_scorer.score_sentiment.assert_called_with([
            ([], "great"),
            ([], "uncomfortable")])

    def test_score_sentiment_adds_scores_for_matched_phrases_with_multiple_words(self):
        text = "It didn't work for us."
        self._sentiment_analyser.score_sentiment(text)
        self._sentiment_scorer.score_sentiment.assert_called_with([
            ([], "didn't work")])

    def test_score_sentiment_matches_phrases_case_insensitive(self):
        text = "Great, great, GREAT"
        self._sentiment_analyser.score_sentiment(text)
        self._sentiment_scorer.score_sentiment.assert_called_with([
            ([], "great"),
            ([], "great"),
            ([], "great")])

    def test_score_sentiment_not_matches_partial_words(self):
        text = "The room was cold, but it was hardly a problem"
        self._sentiment_analyser.score_sentiment(text)
        self._sentiment_scorer.score_sentiment.assert_called_with([])

    def test_score_sentiment_multiplies_phrase_score_by_preceding_multiplier_scores(self):
        text = "The location was NOT really great, but it was not bad either"
        self._sentiment_analyser.score_sentiment(text)
        self._sentiment_scorer.score_sentiment.assert_called_with([
            (["not", "really"], "great"),
            (["not"], "bad")])

    def test_score_sentiment_multiplies_phrase_score_correctly_when_term_multiple_times(self):
        text = "The location was great, actually it was really great!"
        self._sentiment_analyser.score_sentiment(text)
        self._sentiment_scorer.score_sentiment.assert_called_with([
            ([], "great"),
            (["really"], "great")])

    def test_score_sentiment_when_no_multipliers_then_find_no_multipliers(self):
        text = "The location was really great!"
        self._sentiment_analyser.initialize({"great" : 2})
        self._sentiment_analyser.score_sentiment(text)
        self._sentiment_scorer.score_sentiment.assert_called_with([
            ([], "great")])

    def test_score_sentiment_when_no_sentiment_weights_then_find_no_blocks(self):
        text = "The location was really great!"
        self._sentiment_analyser.initialize({})
        self._sentiment_analyser.score_sentiment(text)
        self._sentiment_scorer.score_sentiment.assert_called_with([])

if __name__ == '__main__':
    unittest.main()