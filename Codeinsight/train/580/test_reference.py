def test(dict0, var0, var1):
    if var0 not in dict0:
        dict0[var0] = []
    dict0[var0].append(var1)
    return dict0

