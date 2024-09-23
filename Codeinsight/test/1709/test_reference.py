def test(dict0, key0):
    if dict0.get(key0) is None:
        dict0[key0] = 0
    return dict0
