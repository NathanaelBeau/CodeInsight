import pandas as pd

def test(df0, col_name0, lst0):
    return df0[df0[col_name0].isin(lst0)]
