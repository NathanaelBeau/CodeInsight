import pandas as pd

def test(df0, col_condition, condition_val, col_update, new_val):
    df0.loc[df0[col_condition] >= condition_val, col_update] = new_val
    return df0
