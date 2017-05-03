# TODO: use some dictionairy API
def get_singular_or_plural(word):
    """ Returns singular or plural form (or None)
    """
    
    if word in ["personnel", "staff"]:
        return None
    if word[-1:] == "y":
        return word[:-1] + "ies"
    if word[-3:] == "ies":
        return word[:-3] + "y"
    if word[-1:] == "s":
        return word[:-1] 
    else:
        return word + "s" 

synonyms = {
    "staff" : ["personnel"],
    "personnel" : ["staff"],
    "lavatory" : ["toilet"],
    "toilet" : ["lavatory"]
}

# TODO: use some dictionairy API
def get_synonyms(word):
    """ Returns a list of synonyms
    """
    return synonyms.get(word, [])
    
