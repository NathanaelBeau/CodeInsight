def test(lst0):
    return list(filter(lambda x: lst0.index(x) < 10, lst0))
