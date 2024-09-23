import pandas as pd

def test(df0, var0, var1):
    df0.columns.values[var0] = var1
    return df0

