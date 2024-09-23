import pandas as pd

def test(df0, df1, col_names_df0, col_names_df1):
    df0[col_names_df0] = df1[col_names_df1]
    return df0

