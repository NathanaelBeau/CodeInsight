import pandas as pd

def test(df0, col0, col1):
    df0[col0].fillna(df0[col1], inplace=True)
    return df0