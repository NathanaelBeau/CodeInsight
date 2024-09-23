def test(dict0):
    return [k for k, v in dict0.items() for _ in range(v)]
