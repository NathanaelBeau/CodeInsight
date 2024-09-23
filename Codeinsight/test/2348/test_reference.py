def test(var0, var1):
    return var1.groupby(var0).sum().reset_index()
