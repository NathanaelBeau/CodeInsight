def test(lst0):
    return set().union(*(d.keys() for d in lst0))
