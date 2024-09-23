def test(dict0, dict1):
    return all(dict0.get(key) == dict1.get(key) for key in dict0.keys()) and all(dict1.get(key) == dict0.get(key) for key in dict1.keys())

