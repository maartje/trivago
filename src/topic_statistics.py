class TopicStatistics:

    def __init__(self, sentences):
        self._sentences = sentences
        self._sentences.sort_values("Score", inplace=True, ascending=False)

    def mean_score_per_hotel(self):
        scores_per_hotel = self._sentences.groupby(level="HotelID")[["Score"]].mean().sort_values("Score", ascending=False)
        scores_per_hotel.columns = ["Score"]
        scores_per_hotel.reset_index(inplace=True)
        return scores_per_hotel
        
    def most_positive_sentences(self, top=3):
        return self._sentences.head(top)
        
    def most_negative_sentences(self, top=3):
        return self._sentences.tail(top)
    
        