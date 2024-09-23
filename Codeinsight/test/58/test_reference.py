import json

def test(str0):
    json_acceptable_string = str0.replace("'", "\"")
    d = json.loads(json_acceptable_string)
    return d
