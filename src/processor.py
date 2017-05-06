import re
import pandas as pd
from pandas.io.json import json_normalize

class Processor:
    
    def __init__(self, data_loader, sentiment_analyser):
        self._data_loader = data_loader
        self._sentiment_analyser = sentiment_analyser
        self._semantic_weights = {}
        self._intensifier_weights = {}
        self.word_table = {} 
        self.review_sentences = None
        self._split_regex = re.compile("[\.\!\?\,\;]")
    
    def _process_review_file(self, review_file):
            review_data = self._data_loader.load_json(review_file)
            hotel = self._get_hotel(review_data)
            reviews = self._get_reviews(review_data, hotel)
            review_sentences = self._get_review_sentences(reviews)
            print (len(reviews), "reviews processed for:", review_file)
            return review_sentences
        

    def process(self, review_files, semantic_file):
        semantics_data = self._data_loader.load_json(semantic_file)
        self._semantic_weights = self._get_semantic_weights(semantics_data)
        self._intensifier_weights = self._get_intensifier_weights(semantics_data)
        self._sentiment_analyser.initialize(self._semantic_weights, self._intensifier_weights)
        print (len(self._semantic_weights), "phrases detected")
        print (len(self._intensifier_weights), "intensifiers detected")

        review_sentence_frames = [self._process_review_file(review_file) for review_file in review_files]
        self.review_sentences = pd.concat(review_sentence_frames)

        print (len(self.review_sentences), "review sentences analysed in total")
        

        self._score_review_sentences()
        self.word_table = self._build_word_table()

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

    def _get_hotel(self, review_data):
        hotel = review_data['HotelInfo']
        return hotel

    def _get_reviews(self, review_data, hotel):
        df_reviews = json_normalize(review_data['Reviews'])
        df_reviews["HotelID"] = hotel.get("HotelID", "Unknown")
        df_reviews.set_index(["HotelID", "ReviewID"], inplace=True)
        return df_reviews
    
    def _get_review_sentences(self, reviews):
        df_reviews_sentences = reviews["Content"].apply(
            lambda c: [s.strip() for s in self._split_regex.split(c)]
        ).apply(pd.Series).stack().to_frame()
        df_reviews_sentences.index.rename(["HotelID", "ReviewID", "SentenceNumber"], inplace=True)
        df_reviews_sentences.columns = ["Sentence"]
        return df_reviews_sentences

    def _score_review_sentences(self):
        self.review_sentences["Score"] = self.review_sentences["Sentence"].apply(
            lambda s: self._sentiment_analyser.score_sentiment(s)
        )
    
    def _build_word_table(self):
        word_pattern = r"[\W]+"
        regex = re.compile(word_pattern)
        
        word_table = {}
        for index, sentence in self.review_sentences["Sentence"].iteritems():
            words = regex.split(sentence.strip().lower())
            for w in words:
                indices_for_word = word_table.get(w, set())
                indices_for_word.add(index)
                word_table[w] = indices_for_word
        print (len(word_table.keys()), "words stored in lookup table")
        return word_table
