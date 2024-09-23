import pandas as pd

def test(df0, df1, col_names_df0, col_names_df1):
    new_df1 = df1[col_names_df1].rename(columns=dict(zip(col_names_df1, col_names_df0)))
    return df0.join(new_df1)

