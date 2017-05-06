class TopicStatistics:

    def __init__(self, sentences):
        self._sentences = sentences
        self._sentences.sort_values("Score", inplace=True, ascending=False)
        self._group_by_hotel = self._sentences.groupby(level="HotelID")
    
    def compare_hotels(self):
        result = self._group_by_hotel.agg(['mean', 'count'])
        result.columns = ["Score", "#Fragments"]
        result.reset_index(inplace=True)
        result.sort_values("Score", ascending=False)
        return result
        
    def most_positive_sentences(self, top=3):
        return self._sentences.head(top)
        
    def most_negative_sentences(self, top=3):
        return self._sentences.tail(top)
    
        