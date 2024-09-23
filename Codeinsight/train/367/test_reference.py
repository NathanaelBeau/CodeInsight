def test(lst0, lst1):
    return list(map(lambda a, b: a is b, lst0, lst1))
