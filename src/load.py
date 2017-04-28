import json

def load_json(path):
    with open(path) as data_file:    
        data = json.load(data_file)
        return data