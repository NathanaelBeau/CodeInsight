def test(lst0):
    return [set(item) for item in set(frozenset(item) for item in lst0)]

