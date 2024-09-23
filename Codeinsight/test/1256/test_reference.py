import pandas as pd

def test(df0, var0):
    return df0.columns[df0.isin([var0]).any()].tolist()
