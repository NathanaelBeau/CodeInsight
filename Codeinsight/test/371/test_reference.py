import pandas as pd

def test(df0, column_name0, value_list0):
    return df0[df0[column_name0].isin(value_list0)]

