import pandas as pd

def test(df0, lst0, var0):
    df0[var0] = df0[lst0].sum(axis=1)
    return df0

