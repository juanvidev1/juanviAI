import json

def load_data():
    with open('nlp_responses.json', 'r') as f:
        data = json.load(f)
    return data