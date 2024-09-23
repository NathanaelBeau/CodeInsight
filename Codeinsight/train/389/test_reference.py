def test(df0):
    return df0[(df0['A'] > 1) | (df0['B'] < -1)]