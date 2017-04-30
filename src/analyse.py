import re

def score_sentiment(text, weights, topic_words = []):
    if not topic_words:
        return _calculate_sentiment_score(text, weights)
    pattern_prefix = r"([^a-zA-Z]|^)" #make sure that a full word is matched, i.e. do not match 'old' in 'cold'
    pattern_suffix = r"s?([^a-zA-Z]|$)" #make sure that a full word is matched, i.e. do not match 'hard' in 'hardly', support plural form
    pattern = pattern_prefix + "|".join(topic_words) + pattern_suffix
    regex = re.compile(pattern, re.IGNORECASE)
    sentences = text.split(".") #TODO: ! ? (,;)
    topic_sentences = [s for s in sentences if regex.search(s)]
    scores_topic_sentences = [_calculate_sentiment_score(s, weights) for s in topic_sentences]
    return sum(scores_topic_sentences)

def _calculate_sentiment_score(text, weights):
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
