import random

def test(dict0):
    keys = list(dict0.keys())
    weights = list(dict0.values())
    return random.choices(keys, weights=weights)[0]
