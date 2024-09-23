def test(var0, var1):
    i = 0
    while i < len(var0) and i < len(var1) and var0[i] == var1[i]:
        i += 1
    return var0[:i]

