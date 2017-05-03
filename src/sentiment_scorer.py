import operator
import functools

class SentimentScorer:
    """ Calculates a sentiment score for sentiment phrases and their associated multipliers"""

    def __init__(self):
        """Initializes SentimentScorer."""
        self._sentiment_weights = {}
        self._multiplier_weights = {}

    def initialize(self, sentiment_weights={}, multiplier_weights = {}):
        self._sentiment_weights = sentiment_weights
        self._multiplier_weights = multiplier_weights

    def score_sentiment(self, sentiment_blocks):
        return sum ([self._score_sentiment_block(b) for b in sentiment_blocks])

    def _score_sentiment_block(self, block):
        (multipliers, phrase) = block
        phrase_weight = (self._sentiment_weights.get(phrase, 0))
        mult_weights = ([self._multiplier_weights.get(m, 1) for m in multipliers])
        block_score = functools.reduce(operator.mul, mult_weights + [phrase_weight], 1)
        return block_score
