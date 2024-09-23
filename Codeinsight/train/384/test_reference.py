def test(df0):
    df0.drop(df0.columns[[0, 1, 3]], axis=1, inplace=True)
    return df0
