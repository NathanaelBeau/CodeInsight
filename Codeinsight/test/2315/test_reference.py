import pandas as pd

def test(df0, df1, df2, col_name):
    return df0.merge(df1, on=col_name).merge(df2, on=col_name)

