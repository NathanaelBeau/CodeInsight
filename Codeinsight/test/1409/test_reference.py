import pandas as pd

def test(df0, lst0, var0):
    return df0[df0.loc[:, var0].isin(lst0)]
