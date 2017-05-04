""" Main

Usage:
  main.py <path> <path>
  
  First argument is the path to the directory (or file) containing the hotel reviews in json format.
  Second argument (optional) is the topic.
  Third argument (optional) is the path to the file containing the semantics in json format.
"""

import sys
from processor import Processor
from data_loader import DataLoader
from sentiment_analyser import SentimentAnalyzer
from sentiment_scorer import SentimentScorer
from language_service import LanguageService
from topic_locator import TopicLocator
from application import Application

def main(path_to_reviews, topic=None, semantic_file = "semantics/semantics.json"):  
    data_loader = DataLoader()
    sentiment_scorer = SentimentScorer()
    sentiment_analyser = SentimentAnalyzer(sentiment_scorer)

    review_files = path_to_reviews #TODO dir
    processor = Processor(data_loader, sentiment_analyser)
    processor.process(review_files, semantic_file)
    
    language_service = LanguageService()
    word_table = processor._word_table #TODO: public
    topic_locator = TopicLocator(language_service, word_table)
    # indices = topic_locator.get_topic_indices("room")
    # print indices[0:3]
    review_sentences = processor._review_sentences #TODO public
    application = Application(topic_locator, review_sentences)
    return application

    # ds = df_reviews['Content'].apply(lambda t: score_sentiment(t, weights, topic_words))
    # ds.sort_values(inplace=True)
    # print(ds.values[0], ds.values[-1]) 
    

if __name__ == "__main__":
    if len(sys.argv) == 3:
        application = main(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 2:
        application = main(sys.argv[1])
    if len(sys.argv) == 1:
        application = main(["data/reviews2.json", "data/reviews1.json"])
    else:
        raise ValueError('Wrong number of arguments. Arguments are: path to reviews directory (optional) and path to semantics file (optional)')
    while True:
        topic = input('Enter your topic word:')
        topic_statistics = application.analyze_sentiment(topic)
        hotel_scores = topic_statistics.mean_score_per_hotel()
        print(hotel_scores)
