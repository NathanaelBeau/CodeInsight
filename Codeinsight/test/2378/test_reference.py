def test(lst0, lst1):
    return list(map(lst0.__getitem__, lst1))