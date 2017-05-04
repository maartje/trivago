""" Main

Usage:
  python src/main.py <dir-path> <file-path>
  
  First argument is the path to the directory containing the hotel reviews in json format.
  Second argument (optional) is the path to the file containing the semantics in json format.
"""

import sys
from processor import Processor
from data_loader import DataLoader
from sentiment_analyser import SentimentAnalyzer
from sentiment_scorer import SentimentScorer
from language_service import LanguageService
from topic_locator import TopicLocator
from application import Application
import os

def main(reviews_dir, topic=None, semantic_file = "semantics/semantics.json"):  
    review_paths = get_filepaths_in_dir(reviews_dir)
    data_loader = DataLoader()
    sentiment_scorer = SentimentScorer()
    sentiment_analyser = SentimentAnalyzer(sentiment_scorer)
    processor = Processor(data_loader, sentiment_analyser)
    processor.process(review_paths, semantic_file)
    
    word_table = processor.word_table 
    review_sentences = processor.review_sentences 
    language_service = LanguageService()
    topic_locator = TopicLocator(language_service, word_table)
    application = Application(topic_locator, review_sentences)
    return application

def get_filepaths_in_dir(dir):
    files = os.listdir(dir)
    file_paths = [os.path.join(dir, file) for file in files]
    file_paths.sort()
    return file_paths
    

if __name__ == "__main__":
    if len(sys.argv) == 3:
        application = main(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 2:
        application = main(sys.argv[1])
    if len(sys.argv) == 1:
        application = main("data")
    else:
        raise ValueError('Wrong number of arguments. Arguments are: path to reviews directory (optional) and path to semantics file (optional)')
    while True:
        topic = input("Enter your topic word: ")
        topic_statistics = application.analyze_sentiment(topic)
        hotel_scores = topic_statistics.mean_score_per_hotel()
        print(hotel_scores)
