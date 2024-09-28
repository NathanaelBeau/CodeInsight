import pandas as pd

def test(df0, column_name0):
    counts = df0[column_name0].value_counts()
    return counts.values

