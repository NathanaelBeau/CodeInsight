import pandas as pd

def test(df0, var0, var1, var2, var3):
    return df0[(df0[var0] == var1) & (df0[var2] == var3)].reset_index(drop=True)

