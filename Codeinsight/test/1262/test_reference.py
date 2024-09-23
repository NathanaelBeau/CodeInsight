import pandas as pd

def test(df0, col_name):
    column_sum = df0[col_name].sum()
    column_length = len(df0[col_name])
    return column_sum / column_length

