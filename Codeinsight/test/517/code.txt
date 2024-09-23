import pandas as pd

def test(df0, col0, var0, var1):
    df0[col0].replace(var0, var1, inplace=True)
    return df0
