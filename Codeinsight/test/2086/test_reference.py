import pandas as pd

def test(df0):
    return df0.groupby('A').agg({'B': ['sum', 'count']})

