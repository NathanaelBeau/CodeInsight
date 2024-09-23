import pandas as pd

def test(df0, col0, var0, var1):
    df0.loc[df0[col0] == var0, col0] = var1
    return df0

