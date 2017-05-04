class LanguageService:

    def __init__(self):
        # for illustration purpose only
        self._synonyms = {
            "staff" : ["personnel"],
            "personnel" : ["staff"],
            "lavatory" : ["toilet"],
            "toilet" : ["lavatory"]
        }
        self._plural_only_forms = [
            "personnel", 
            "staff"
        ]


    # TODO: use some dictionairy API
    def get_singular_or_plural(self, word):
        """ Returns singular or plural form (or None)
        """
        if word in self._plural_only_forms:
            return None
        if word[-1:] == "y":
            return word[:-1] + "ies"
        if word[-3:] == "ies":
            return word[:-3] + "y"
        if word[-1:] == "s":
            return word[:-1] 
        else:
            return word + "s" 
    
    
    # TODO: use some dictionairy API
    def get_synonyms(self, word):
        """ Returns a list of synonyms
        """
        return self._synonyms.get(word, [])
        
