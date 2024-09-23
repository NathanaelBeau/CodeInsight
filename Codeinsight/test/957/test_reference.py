import pandas as pd

def test(df0, axis0):
    row_means = dfo.mean(axis=axis0)
    normalized_df = df0.subtract(row_means, axis=0)
    return normalized_df
