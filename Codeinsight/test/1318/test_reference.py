import pandas as pd

def test(df0, str0, lst0):
    df0.loc[str0] = lst0
    return df0
