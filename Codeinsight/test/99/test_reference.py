import pandas as pd
def test(df0, var0, var1, var2):
    df0.loc[df0[var0] == var1, var2] = var1
    return df0

