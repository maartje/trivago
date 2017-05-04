class TopicLocator:

    def __init__(self, language_service, word_table):
        self._language_service = language_service
        self._word_table = word_table

    def get_topic_indices(self, topic):
        topic_words = self._get_topic_words(topic)
        result = set()
        for t in topic_words:
            topic_indices = self._word_table.get(t, [])
            result.union(topic_indices)
        return list(topic_indices)
            

    def _get_topic_words(self, word):
        result = [word.lower()]
        result.extend(self._language_service.get_synonyms(word.lower()))
        result.extend([self._language_service.get_singular_or_plural(w) for w in result])
        return [w for w in result if w]
