import pandas as pd

def test(df0, lst0):
    df0.loc[len(df0)] = lst0
    return df0

