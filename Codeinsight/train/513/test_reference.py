def test(lst0, var0, var1):
    return [(var0[i] if flag else var1[i]) for i, flag in enumerate(lst0)]

