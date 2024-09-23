import pandas as pd

def test(df0, columns_list0, column_name0):
    for col in columns_list0:
        df0[col] = df0[col] / df0[column_name0]
    return df0

