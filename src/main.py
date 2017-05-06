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
import re

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
    if len(sys.argv) > 3:
        raise ValueError('Wrong number of arguments. Arguments are: path to reviews directory (optional) and path to semantics file (optional)')
    if len(sys.argv) == 3:
        application = main(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 2:
        application = main(sys.argv[1])
    if len(sys.argv) == 1:
        application = main("data")
    while True:
        print ()
        topic = input("Enter your topic word:")
        if not re.match("^[a-zA-Z]*$", topic):
            print ("Error: Enter a single topic word or leave empty")
            continue
        topic_statistics = application.analyze_sentiment(topic)
        print()
        print(topic_statistics.compare_hotels())
        print()

        most_positive = topic_statistics.most_positive_sentences(1)
        if len(most_positive) > 0:
            print("Most positive fragment:")
            print (most_positive["Sentence"][0], "(", most_positive["Score"][0] ,")")
            print()
            most_negative = topic_statistics.most_negative_sentences(1)
            print("Most negative fragment:")
            print (most_negative["Sentence"][0], "(", most_negative["Score"][0] ,")")

        
