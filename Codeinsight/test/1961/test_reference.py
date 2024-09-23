def test(dict0):
    keys, values = zip(*dict0.items())
    return list(keys), list(values)
