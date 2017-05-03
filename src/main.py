""" Main

Usage:
  main.py <path> <path>
  
  First argument is the path to the directory (or file) containing the hotel reviews in json format.
  Second argument (optional) is the topic.
  Third argument (optional) is the path to the file containing the semantics in json format.
"""

import sys
from load import load_json
from process import get_weights, get_intensifiers, get_reviews, get_hotel
from analyse import score_sentiment
from language_service import get_singular_or_plural, get_synonyms


def main(reviews, topic=None, semantics = "semantics/semantics.json"):  

    semantics_data = load_json(semantics)
    weights = get_weights(semantics_data)
    df_intensifiers = get_intensifiers(semantics_data)

    review_data = load_json(reviews) 
    df_reviews = get_reviews(review_data)
    hotel = get_hotel(review_data)
    
    topic_words = get_topic_words(topic)
    ds = df_reviews['Content'].apply(lambda t: score_sentiment(t, weights, topic_words))
    ds.sort_values(inplace=True)
    print(ds.values[0], ds.values[-1])    
    
def get_topic_words(word):
    result = [word]
    result.extend(get_synonyms(word))
    result.extend([get_singular_or_plural(w) for w in result])
    return [w for w in result if w]

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
