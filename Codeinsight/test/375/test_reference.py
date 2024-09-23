def test(dict0, var0, var1):
    dict0.setdefault(var0, []).append(var1)
    return dict0
