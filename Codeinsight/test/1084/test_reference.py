def test(dict0, lst0):
    return [key for key, value in dict0.items() if any(item in value for item in lst0)]

