import pandas as pd

def test(df0, var0, cond0, var1):
    df0.loc[df0[var0] == cond0, var0] = var1
    return df0
