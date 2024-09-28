def test(dict0, var0):
    return bool(list(filter(lambda val: val == var0, dict0.values())))
