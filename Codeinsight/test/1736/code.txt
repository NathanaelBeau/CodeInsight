import pandas as pd

def test(df0, var0, dict0):
    df0[var0] = df0[var0].replace(dict0)
    return df0
