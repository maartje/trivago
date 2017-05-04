import pandas as pd
from pandas.io.json import json_normalize

class Processor:
    
    def __init__(self, data_loader):
        self._data_loader = data_loader

        self._semantic_weights = {}
        self._intensifier_weights = {}
        self._hotel = None # TODO: data frame with hotels?
        self._reviews = None
        self._review_sentences = None
        self._words = {} # Todo {'room' : [(R3456, 6)], ...}
        
    def process(self, path_to_reviews, path_to_semantics):
        semantics_data = self._data_loader.load_json(path_to_semantics)
        self._semantic_weights = self._get_semantic_weights(semantics_data)
        self._intensifier_weights = self._get_intensifier_weights(semantics_data)
        
        print (self._semantic_weights.get('great'))
        print (self._intensifier_weights.get('not'))
        
        review_data = self._data_loader.load_json(path_to_reviews)
        self._hotel = self._get_hotel(review_data)
        self._reviews = self._get_reviews(review_data)
        self._review_sentences = self._get_review_sentences(self._reviews)

        print (self._hotel)
        print(self._reviews.loc[["UR139956543"]]["Content"][0])
        print(self._review_sentences.loc[[("UR139956543", 3)]])
    
    def _get_semantic_weights(self, semantics_data):
        df_positive = json_normalize(semantics_data['positive'])
        df_negative = json_normalize(semantics_data['negative'])
        df_negative['value'] = df_negative['value'].apply(lambda v: -1*v)
        df_weights = pd.concat([df_negative, df_positive])
        weights = dict(zip(df_weights['phrase'], df_weights['value']))
        return weights
    
    def _get_intensifier_weights(self, semantics_data):
        df_intensifiers = json_normalize(semantics_data['intensifier'])
        intensifiers = dict(zip(df_intensifiers['phrase'], df_intensifiers['multiplier']))
        return intensifiers

    def _get_reviews(self, review_data):
        df_reviews = json_normalize(review_data['Reviews'])
        df_reviews.set_index(["ReviewID"], inplace=True)
        return df_reviews
    
    def _get_hotel(self, review_data):
        hotel = review_data['HotelInfo']
        return hotel
    
    def _get_review_sentences(self, df_reviews):
        df_reviews_sentences = df_reviews["Content"].apply(lambda c: c.split(".")).apply(pd.Series).stack().to_frame()
        df_reviews_sentences.index.rename(["ReviewID", "SentenceNumber"], inplace=True)
        df_reviews_sentences.columns = ["Sentence"]
        return df_reviews_sentences
