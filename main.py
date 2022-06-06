import requests
import json
url = "https://uselessfacts.jsph.pl/random.json?language=en"

class Fact():
    def get_fact():
        #global data
        response = requests.request('GET',url)
        data = json.loads(response.text)
        fact = data['text']
        return fact
