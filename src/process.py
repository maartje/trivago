import pandas as pd
from pandas.io.json import json_normalize

def get_weights(semantics_data):
    df_positive = json_normalize(semantics_data['positive'])
    df_negative = json_normalize(semantics_data['negative'])
    df_negative['value'] = df_negative['value'].apply(lambda v: -1*v)
    df_weights = pd.concat([df_negative, df_positive])
    return df_weights

def get_intensifiers(semantics_data):
    df_intensifier = json_normalize(semantics_data['intensifier'])
    return df_intensifier

def get_reviews(review_data):
    df_reviews = json_normalize(review_data['Reviews'])
    return df_reviews

def get_hotel(review_data):
    hotel = review_data['HotelInfo']
    return hotel
    