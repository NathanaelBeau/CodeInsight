import pandas as pd

def test(df0, lst0, var0):
    return df0[df0.apply(lambda row: row[var0] in lst0, axis=1)]

