def test(lst0, lst1):
    return sorted(lst0, key=lambda x: lst1.index(x[0]))
