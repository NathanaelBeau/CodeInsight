import pandas as pd

def test(df0, var0):
    return df0[(df0[var0].isna()) | (df0[var0] == 'Other')]
