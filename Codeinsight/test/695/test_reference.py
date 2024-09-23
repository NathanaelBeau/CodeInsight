def test(var0, var1, df0):
    df0[var1] = df0.apply(lambda row: var0(row), axis=1)
    return df0
