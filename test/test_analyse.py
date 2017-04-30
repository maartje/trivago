from src.analyse import score_sentiment
import unittest

class TestStringMethods(unittest.TestCase):

    def test_score_sentiment_adds_scores_for_matched_phrases(self):
        text = "The location was great, but the bed uncomfortable"
        actual_score = score_sentiment(text, {"uncomfortable" : -1, 'great' : 2})
        expected_score = -1 + 2
        self.assertEqual(actual_score, expected_score)

    def test_score_sentiment_adds_scores_for_matched_phrases_with_multiple_words(self):
        text = "It didn't work for us."
        actual_score = score_sentiment(text, {"didn't work" : -1})
        expected_score = -1
        self.assertEqual(actual_score, expected_score)

    def test_score_sentiment_matches_phrases_case_insensitive(self):
        text = "Great, great, GREAT"
        actual_score = score_sentiment(text, {"uncomfortable" : -1, 'great' : 2})
        expected_score = 2 + 2 + 2
        self.assertEqual(actual_score, expected_score)

    def test_score_sentiment_not_matches_partial_words(self):
        text = "The room was cold, but it was hardly a problem"
        actual_score = score_sentiment(text, {"old" : -1, 'hard' : -1})
        expected_score = 0
        self.assertEqual(actual_score, expected_score)

if __name__ == '__main__':
    unittest.main()