import pandas as pd 

def test(df0, var0):
    df0[var0] = df0[var0].astype(int)
    return df0

