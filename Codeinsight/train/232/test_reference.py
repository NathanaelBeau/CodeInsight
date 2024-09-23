def test(lst1):
    return [(lambda x: x if x >= 0 else 0)(x) for x in lst1]
