def test(df0):
    return df0.groupby(df0.index).sum()
