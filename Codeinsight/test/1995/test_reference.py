import pandas as pd

def test(df0, col0):
    df0[col0] = df0[col0].str.upper()
    return df0

