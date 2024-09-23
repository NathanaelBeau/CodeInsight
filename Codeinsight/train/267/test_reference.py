import pandas as pd

def test(df0, var2,var0 = -12, var1 = None):
    if var1 is None:
        var1 = df0.shape[1]
    return df0[(df0.iloc[:, var0:var1] == var2).any(axis=1)]

