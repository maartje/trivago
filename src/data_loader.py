import json

class DataLoader:
    
    def load_json(self, path):
        with open(path) as data_file:    
            data = json.load(data_file)
            return data