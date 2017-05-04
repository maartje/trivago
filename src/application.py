class Application:
    
    def __init__(self, topic_locator, review_sentences, reviews=None, hotels=None):
        self._topic_locator = topic_locator
        self._review_sentences = review_sentences
        
    def analyze_sentiment(self, topic):
        topic_indices = self._topic_locator.get_topic_indices(topic)
        topic_sentences = self._review_sentences.loc[topic_indices]
        return {
            "mean" : round(topic_sentences['Score'].mean(), 2)
        }
