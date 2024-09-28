def test(lst0, lst1):
    for item in reversed(lst1):
        lst0.insert(0, item)
    return lst0