import json

def test(lst0):
    unique_dicts = [json.loads(x) for x in set([json.dumps(d, sort_keys=True) for d in lst0])]
    unique_dicts.sort(key=lst0.index)
    return unique_dicts
