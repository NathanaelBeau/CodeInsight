import pandas as pd

def test(df0, lst0):
    df0.drop(lst0, inplace=True, errors='ignore')
    return df0
