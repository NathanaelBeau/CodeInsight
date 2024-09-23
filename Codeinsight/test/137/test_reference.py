import pandas as pd

def test(df0, var0):
    df0[var0] = df0[var0].str.lower()
    return df0
