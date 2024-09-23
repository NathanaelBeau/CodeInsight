def test(lst0, lst1):
    return all(item in lst1 for item in lst0)