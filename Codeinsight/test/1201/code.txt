def test(lst0, lst1):
    return list(map(sum, zip(lst0, lst1)))