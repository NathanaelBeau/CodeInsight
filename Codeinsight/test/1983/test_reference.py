import pandas as pd

def test(df0, var0):
    df0[var0] = df0[var0].fillna(0)
    return df0

