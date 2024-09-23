def test(lst0):
    return [list(x) for x in set(tuple(x) for x in lst0)]
