def test(lst0):
    iterator = iter(lst0)
    result = dict(zip(iterator, iterator))
    return result