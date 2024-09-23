import pandas as pd

def test(df0, var0):
    return df0.groupby(var0).agg(['count', 'mean', 'sum', 'min', 'max'])
