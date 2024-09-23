import pandas as pd

def test(df0, var0, var1, var2):
    df0.iloc[var0, var1] = var2
    return df0
