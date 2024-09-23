import pandas as pd

def test(df0, column_name0):
    return df0.groupby(column_name0).sum().reset_index()
