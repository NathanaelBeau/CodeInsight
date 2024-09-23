def test(lst0, lst1):
    return all(x in lst1 for x in lst0)
