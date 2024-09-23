def test(lst0, lst1):
    i = 0
    while i < len(lst1):
        lst0.insert(i, lst1[i])
        i += 1
    return lst0
