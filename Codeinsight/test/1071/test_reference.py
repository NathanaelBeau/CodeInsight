import pandas as pd

def test(df0, var0='X'):
    return df0.loc[:, df0.columns.str.startswith(var0)]

