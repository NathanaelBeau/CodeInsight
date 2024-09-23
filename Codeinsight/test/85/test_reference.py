def test(dict0):
    return all(value for value in dict0.values() if isinstance(value, bool))

