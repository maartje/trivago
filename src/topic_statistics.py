class TopicStatistics:

    def __init__(self, sentences):
        self._sentences = sentences
        
    def mean_score_per_hotel(self):
        scores_per_hotel = self._sentences.groupby(level="HotelID")[["Score"]].mean().sort_values("Score", ascending=False)
        scores_per_hotel.columns = ["Score"]
        scores_per_hotel.reset_index(inplace=True)
        return scores_per_hotel
        
    
        