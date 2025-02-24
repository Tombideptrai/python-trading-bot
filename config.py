import json 

class APIKeys:

    def __init__(self, key_file = "keys.json"):

        self.key_file = key_file
        self.load_keys()

    def load_keys(self):

        with open(self.key_file, 'r') as file:

            self.keys = json.load(file)

    def get(self, key, default = None):

        return self.keys.get(key, default)
    
#api_keys = APIKeys()
#api_key = api_keys.get("API_KEY")
#api_secret = api_keys.get("API_SECRET")

#print(api_key)
#print(api_secret)


