import pandas as pd

def test(df0, var0, var1, var2):
    mask = df0.groupby(var0)[var1].transform('sum') == var2
    return df0[mask]