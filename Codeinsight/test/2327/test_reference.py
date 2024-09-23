import pandas as pd

def test(df0, lst0, lst1):
    col_indices = [df0.columns.get_loc(col) for col in lst1]
    return df0.iloc[lst0, col_indices].mean()

