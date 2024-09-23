import pandas as pd

def test(df0):
    df0['new_col'] = range(len(df0))
    return df0
