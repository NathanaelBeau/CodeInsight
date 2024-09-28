def test(lst0, var0):
    return sum(isinstance(i, var0) for i in lst0)
