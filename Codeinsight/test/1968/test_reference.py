import pandas as pd

def test(df0, var0, var1):
    df0.loc[df0[var0] > 2, var1] = new_value
    return df0
