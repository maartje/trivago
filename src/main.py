""" Main

Usage:
  main.py <path> <path>
  
  First argument (optional) is the path to the directory (or file) containing the hotel reviews in json format.
  Second argument (optional) is the path to the file containing the semantics in json format.
"""

import sys
from load import load_json
from process import get_weights, get_intensifiers, get_reviews, get_hotel


def main(reviews = "data/reviews3.json", semantics = "semantics/semantics.json"):
    semantics_data = load_json(semantics)
    df_weights = get_weights(semantics_data)
    df_intensifiers = get_intensifiers(semantics_data)

    review_data = load_json(reviews) #TODO: support passing dir with review files
    df_reviews = get_reviews(review_data)
    hotel = get_hotel(review_data)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    if len(sys.argv) == 2:
        main(sys.argv[1])
    if len(sys.argv) == 1:
        main()
    else:
        raise ValueError('Wrong number of arguments. Arguments are: path to reviews directory (optional) and path to semantics file (optional)')
