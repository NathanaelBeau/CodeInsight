import pandas as pd

def test(df0, col0):
    df0[col0] = df0[col0].astype(str)
    return df0

