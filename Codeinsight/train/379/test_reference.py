import pandas as pd

def test(df0, col0, col1):
    return df0.sort_values(by=[col0, col1], ascending=True)

