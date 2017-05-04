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

def main(path_to_reviews, topic=None, path_to_semantics = "semantics/semantics.json"):  
    data_loader = DataLoader()
    processor = Processor(data_loader)
    processor.process(path_to_reviews, path_to_semantics)

    # ds = df_reviews['Content'].apply(lambda t: score_sentiment(t, weights, topic_words))
    # ds.sort_values(inplace=True)
    # print(ds.values[0], ds.values[-1]) 
    

if __name__ == "__main__": #TODO: topic can be a list with synonyms. 
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 2:
        main(sys.argv[1])
    if len(sys.argv) == 1:
        main("data/reviews2.json", "room") #TODO make path to reviews required? 
    else:
        raise ValueError('Wrong number of arguments. Arguments are: path to reviews directory (optional) and path to semantics file (optional)')
