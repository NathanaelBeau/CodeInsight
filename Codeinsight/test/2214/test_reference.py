def test(lst0, var0):
    return list(filter(lambda x: not var0(x), lst0))
