import re

class SentimentAnalyzer:
    """ Calculates a sentiment score by identifying semantic phrases and multipliers"""

    def __init__(self, scorer):
        """Initializes SentimentAnalyzer."""
        self._scorer = scorer
        self._sentiment_regex = None
        self._multiplier_pattern = None    
        
    def initialize(self, sentiment_weights, multiplier_weights = {}):
        self._scorer.initialize(sentiment_weights, multiplier_weights)
        self._sentiment_regex = self._get_sentiment_regex(sentiment_weights.keys())
        self._multiplier_pattern = self._get_multiplier_pattern(multiplier_weights.keys())    

    def score_sentiment(self, text):
        """ Calculates a sentiment score from sentiment phrases and multipliers """
        sentiment_blocks = self._find_sentiment_blocks(text)
        return self._scorer.score_sentiment(list(sentiment_blocks))

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

    def _get_sentiment_regex(self, sentiment_phrases):
        if not sentiment_phrases:
            never_match_pattern = "a^"
            return re.compile(never_match_pattern) 
        word_start_pattern = r"(?<![a-zA-Z])"
        word_end_pattern = r"(?![a-zA-Z])"
        pattern = word_start_pattern + "("+ "|".join(sentiment_phrases) + ")" + word_end_pattern
        return re.compile(pattern, re.IGNORECASE)

    def _get_multiplier_pattern(self, multipliers):
        if not multipliers:
            never_match_pattern = "a^"
            return never_match_pattern 
        return "(" + "|".join(multipliers) + ")"


