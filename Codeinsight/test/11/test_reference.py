def test(dict0, str0):
    return [value for key, value in dict0.items() if str0.lower() in key.lower()]

