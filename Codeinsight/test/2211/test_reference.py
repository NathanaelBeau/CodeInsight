import pandas as pd

def test(df0, var0, var1, val0, val1):
    return df0[(df0[var0] == val0) & (df0[var1] == val1)]

