def test(lst0, var0, lst1):
    return list(filter(lambda x: x[var0] not in lst1, lst0))

