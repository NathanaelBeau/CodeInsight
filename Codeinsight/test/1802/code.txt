import pandas as pd

def test(df0, col0):
    df0[col0] = df0[col0].astype('category').cat.codes
    return df0