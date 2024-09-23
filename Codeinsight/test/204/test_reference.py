def test(var0, var1, lst0):
    return [*filter(lambda x: x.get(var1) == var0, lst0)]
