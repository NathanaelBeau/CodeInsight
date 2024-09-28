def test(str0, var0, var1):
    return ''.join([var1 if i == var0 else c for i, c in enumerate(str0)])
