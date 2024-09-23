def test(var0, df0):
    return df0.groupby(var0, as_index=False).sum()