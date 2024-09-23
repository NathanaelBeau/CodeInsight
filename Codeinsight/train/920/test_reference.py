import pandas as pd

def test(df0, col0, col1):
    return df0.pivot_table(index=col0, values=col1, aggfunc='sum').reset_index()

