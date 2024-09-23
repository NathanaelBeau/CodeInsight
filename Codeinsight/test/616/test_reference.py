def test(lst0):
    all_keys = set().union(*(d.keys() for d in lst0))
    return all_keys
