import pandas as pd

def test(df0, var0, var1):
    return df0.groupby(var0)[var1].nunique()

