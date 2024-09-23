import json

def test(str0):
    return json.loads(str0.replace("'", '"'))