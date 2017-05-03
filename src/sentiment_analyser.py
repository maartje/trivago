import re
import operator
import functools

class SentimentAnalyzer:
    """ Calculates a sentiment score from sentiment phrases and multipliers"""

    def __init__(self, sentiment_weights, multiplier_weights = {}):
        """Initializes SentimentAnalyzer."""
        self._sentiment_weights = sentiment_weights
        self._multiplier_weights = multiplier_weights
        self._sentiment_regex = self._get_sentiment_regex()
        self._multiplier_pattern = self._get_multiplier_pattern()    

    def score_sentiment(self, text):
        """ Calculates a sentiment score from sentiment phrases and multipliers """
        return sum ([self._score_sentiment_block(b) for b in self._find_sentiment_blocks(text)])

    def _find_sentiment_blocks(self, text):
        sentiment_matches = self._sentiment_regex.finditer(text)
        text_position = 0
        for m in sentiment_matches:            
            phrase_prefix_fragment = text[text_position:m.end()]
            phrase_start = m.start() - text_position
            text_position = m.end()
            yield self._build_sentiment_block(phrase_prefix_fragment, phrase_start)
            
    def _build_sentiment_block(self, phrase_prefix_fragment, phrase_start):
            multipliers = self._find_multipliers(phrase_prefix_fragment, phrase_start)            
            phrase = phrase_prefix_fragment[phrase_start :].lower()            
            return (multipliers, phrase)

    def _find_multipliers(self, phrase_prefix_fragment, phrase_start):
        phrase = phrase_prefix_fragment[phrase_start : ]
        pattern = self._multiplier_pattern + "(?=\s+" + phrase + ")"
        match = re.search(pattern, phrase_prefix_fragment, re.IGNORECASE)
        if not match:
            return []
        return self._find_multipliers(phrase_prefix_fragment, match.start()) + [match.group().lower()]

    def _score_sentiment_block(self, block):
        (multipliers, phrase) = block
        phrase_weight = (self._sentiment_weights.get(phrase, 0))
        mult_weights = ([self._multiplier_weights.get(m, 1) for m in multipliers])
        block_score = functools.reduce(operator.mul, mult_weights + [phrase_weight], 1)
        print (block, block_score)
        return block_score

    def _get_sentiment_regex(self):
        word_start_pattern = r"(?<![a-zA-Z])"
        word_end_pattern = r"(?![a-zA-Z])"
        pattern = word_start_pattern + "("+ "|".join(self._sentiment_weights.keys()) + ")" + word_end_pattern
        return re.compile(pattern, re.IGNORECASE)

    def _get_multiplier_pattern(self):
        if not self._multiplier_weights.keys():
            never_match_pattern = "a^"
            return never_match_pattern 
        return "(" + "|".join(self._multiplier_weights.keys()) + ")"
