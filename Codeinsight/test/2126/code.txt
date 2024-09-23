import pandas as pd

def test(df0, col0, col1):
    return df0.groupby(col0).agg({col1: 'sum'}).reset_index()