import pandas as pd

def test(df0, n0):
    df1 = df0.iloc[:n0]
    df2 = df0.iloc[n0:]
    return df1, df2

