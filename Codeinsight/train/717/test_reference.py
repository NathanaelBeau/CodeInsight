def test(lst0):
    return list(filter(lambda x: not isinstance(x, int), lst0))

