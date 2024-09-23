import pandas as pd

def test(df0, col_name, substring):
    return df0[~df0[col_name].str.contains(substring, na=False)]
