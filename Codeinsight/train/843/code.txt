import pandas as pd

def test(df0, col0, var0=','):
    return df0[col0].str.split(var0, expand=True)
