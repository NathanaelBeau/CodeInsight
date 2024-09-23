import pandas as pd

def test(df0, col_name, format_str):
    df0[col_name] = df0[col_name].dt.strftime(format_str)
    return df0

