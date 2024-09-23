import pandas as pd

def test(df0, col_name, lst0):
    return df0[df0[col_name].isin(lst0)]

