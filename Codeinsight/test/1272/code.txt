import pandas as pd

def test(var0, var1, var2, var3, df0):
    return df0.loc[:, ([var2, var3], [var0, var1])]