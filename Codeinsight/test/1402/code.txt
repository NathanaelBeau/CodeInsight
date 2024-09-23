import pandas as pd

def test(df0, col_name):
    df0[col_name] = df0[col_name].str.replace(r'[^a-zA-Z0-9]', '', regex=True)
    return df0
