import pandas as pd

def test(var0):
    df0 = var0.value_counts().reset_index()
    df0.columns = ['value', 'count']
    return df0
