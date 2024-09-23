import pandas as pd

def test(df0, lst0):
    return df0.loc[:, ~df0.columns.isin(lst0)]

