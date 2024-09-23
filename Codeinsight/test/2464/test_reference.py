import pandas as pd

def test(df0, df1, df2, col_name):
    return df0.set_index(col_name).join(df1.set_index(col_name)).join(df2.set_index(col_name)).reset_index()
