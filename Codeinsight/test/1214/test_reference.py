def test(lst0):
    lst0.sort(key=lambda x: (x[0], len(x[1])))
    return lst0

