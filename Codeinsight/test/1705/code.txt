def test(lst0, lst1, var0):
    return sorted(lst1, key=lambda x: lst0.index(x[var0]))
