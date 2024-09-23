import pandas as pd

def test(df0, var0, var1):
    result = df0.groupby(var0)[var1].idxmax()
    return df0.loc[result]

