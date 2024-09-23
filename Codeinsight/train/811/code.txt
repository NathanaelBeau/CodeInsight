import pandas as pd

def test(df0):
    transposed = df0.T
    transposed.columns = range(transposed.shape[1])
    return transposed.reset_index(drop=True)
