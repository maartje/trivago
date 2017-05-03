import re

word_start = r"([^a-zA-Z]|^)"
word_end = r"([^a-zA-Z]|$)"

def score_sentiment(text, weights, topic_words = []):
    if not topic_words:
        return _calculate_sentiment_score(text, weights)
    pattern = word_start + "|".join(topic_words) + word_end
    regex = re.compile(pattern, re.IGNORECASE)
    sentences = text.split(".") #TODO: ! ? (,;)
    topic_sentences = [s for s in sentences if regex.search(s)]
    scores_topic_sentences = [_calculate_sentiment_score(s, weights) for s in topic_sentences]
    return sum(scores_topic_sentences)

def _calculate_sentiment_score(text, weights):
    sentiment_phrases = weights.keys()
    total_score = 0
    pattern = word_start + "(" + "|".join(sentiment_phrases)  + ")" + word_end
    regex = re.compile(pattern, re.IGNORECASE)
    sentiment_matches = regex.finditer(text)
    for r in sentiment_matches:
        phrase = r.group(2)
        score = weights.get(phrase.lower()) 
        total_score += score
    return total_score
