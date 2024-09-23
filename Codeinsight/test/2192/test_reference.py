import pandas as pd

def test(df0, col, str0):
    df0[col] = str0 + df0[col].astype(str)
    return df0

