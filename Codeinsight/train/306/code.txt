import pandas as pd

def test(df0, var0, var1, var2):
    df0[var0] = df0[var1] / df0[var2]
    return df0
