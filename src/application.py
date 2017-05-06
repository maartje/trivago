from topic_statistics import TopicStatistics

class Application:
    
    def __init__(self, topic_locator, review_sentences, reviews=None, hotels=None):
        self._topic_locator = topic_locator
        self._review_sentences = review_sentences
        
    def analyze_sentiment(self, topic):
        if not topic.strip():
            print (len(self._review_sentences), "sentences found")
            return TopicStatistics(self._review_sentences)
        topic_indices = self._topic_locator.get_topic_indices(topic)
        topic_sentences = self._review_sentences.loc[topic_indices]
        return TopicStatistics(topic_sentences)
        # scores = topic_sentences['Score']
        # number_of_sentences = len(scores)
        # number_of_positive_sentences = len(scores[scores >= 0])
        # number_of_negative_sentences = number_of_sentences - number_of_positive_sentences
        # return {
        #     "mean" : round(scores.mean(), 2),
        #     # "number of sentences for topic" : number_of_sentences,
        #     # "number of positive sentences" : number_of_positive_sentences, 
        #     # "number of negative sentences" : number_of_negative_sentences,
        #     # "percentage positive sentences" : round(100.0 * number_of_positive_sentences / number_of_sentences), 
        #     # "percentage negative sentences" : round(100.0 * number_of_negative_sentences / number_of_sentences),
        # }
        

