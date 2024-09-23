def test(dict0):
    return len(dict0) + sum(len(v) for v in dict0.values())

