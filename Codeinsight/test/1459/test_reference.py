import pandas as pd

def test(df0, lst0):
    return df0[list(lst0)].max(axis=1)
