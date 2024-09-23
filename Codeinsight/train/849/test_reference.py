import pandas as pd

def test(df0, lst0):
    df0['max_value'] = df0[lst0].max(axis=1)
    return df0

