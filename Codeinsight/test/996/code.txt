import pandas as pd

def test(df0, col0):
    df0.loc[:, col0] = df0[col0].shift(-1)
    return df0
