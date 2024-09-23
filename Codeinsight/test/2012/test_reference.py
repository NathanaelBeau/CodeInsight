import pandas as pd

def test(df0, var0, lst0):
    return df0[df0[var0].isin(lst0)]
