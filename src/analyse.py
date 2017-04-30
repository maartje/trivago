import re

def score_sentiment(text, weights):
    sentiment_phrases = weights.keys()
    total_score = 0
    pattern_prefix = r"([^a-zA-Z]|^)" #make sure that a full word is matched, i.e. do not match 'old' in 'cold'
    pattern_suffix = r"([^a-zA-Z]|$)" #make sure that a full word is matched, i.e. do not match 'hard' in 'hardly'
    pattern = pattern_prefix + "(" + "|".join(sentiment_phrases)  + ")" + pattern_suffix
    regex = re.compile(pattern, re.IGNORECASE)
    sentiment_matches = regex.finditer(text)
    for r in sentiment_matches:
        phrase = r.group(2)
        score = weights.get(phrase.lower()) #TODO: multipliers
        total_score += score
    return total_score
