import pandas as pd

def test(df0, col_name, substring):
    query_str = f'not {col_name}.str.contains("{substring}")'
    return df0.query(query_str)
