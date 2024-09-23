import pandas as pd

def test(df0, var0):
    df0[var0] = df0[var0].str.split(',')
    return df0.explode(var0)[var0].reset_index(drop=True)

