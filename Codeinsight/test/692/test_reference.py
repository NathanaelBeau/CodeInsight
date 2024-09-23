import pandas as pd

def test(df0, var0):
    return df0.agg({var0: 'sum'})[var0]

