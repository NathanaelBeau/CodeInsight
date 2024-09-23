def test(dict0, lst0):
    return sorted(dict0.items(), key=lambda e: e[1][lst0])

