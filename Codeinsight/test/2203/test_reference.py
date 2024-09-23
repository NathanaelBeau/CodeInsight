def test(dict0, dict1):
    return all(item in dict1.items() for item in dict0.items())

