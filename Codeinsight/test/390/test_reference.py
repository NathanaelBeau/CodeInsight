def test(dict0, var0):
    return sum(1 for x in dict0.values() if var0(x))
