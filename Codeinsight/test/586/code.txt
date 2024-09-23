import pandas as pd

def test(df0, col0, col1):
    df0[col0] = df0[col0].combine_first(df0[col1])
    return df0