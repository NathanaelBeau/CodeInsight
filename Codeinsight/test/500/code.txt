import pandas as pd

def test(df0, var0, lst0, var1):
    df0[var0] = df0[var0].replace(lst0, var1)
    return df0
