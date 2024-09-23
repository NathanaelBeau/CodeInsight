import pandas as pd

def test(df0, var0, str0):
    df0[var0] = df0[var0].str.replace(str0, '')
    return df0


