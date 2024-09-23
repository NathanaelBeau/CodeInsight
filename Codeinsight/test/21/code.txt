import pandas as pd

def test(df0, var0, var1, var2):
    df0[var2] = df0[var2].replace({0: var0, 1: var1})
    return df0
