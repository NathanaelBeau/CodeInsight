def test(var0, var1, var2):
    return [tuple([var0, var1] + var2) for var0, var1, var2 in zip(var0, var1, var2)]

