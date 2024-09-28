import pandas as pd

def test(df0, new_column_tuple0, values_list0):
    df0[new_column_tuple0] = values_list0
    return df0
