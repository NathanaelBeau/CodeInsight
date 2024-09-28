def test(lst0, lst1):
    lst1.reverse()
    for item in lst1:
        lst0.insert(0, item)
    return lst0