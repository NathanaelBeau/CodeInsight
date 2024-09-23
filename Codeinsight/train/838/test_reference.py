import pandas as pd

def test(df0, columns_list0, column_name0):
    df0[columns_list0] = df0[columns_list0].div(df0[column_name0], axis=0)
    return df0

