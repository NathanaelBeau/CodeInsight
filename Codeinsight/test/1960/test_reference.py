import pandas as pd

def test(df0, var0, var1, var2, var3):
    df0[[var1, var2]] = df0[var0].str.split(var3, expand=True)
    return df0

