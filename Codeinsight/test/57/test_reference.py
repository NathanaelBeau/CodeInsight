def test(df0):
    return df0.div(df0.sum(axis=1), axis=0)

