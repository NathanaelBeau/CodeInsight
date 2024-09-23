import pandas as pd

def test(df0, var0):
    sorted_df = df0.sort_values(by=var0)
    sorted_df.index = range(len(sorted_df))
    return sorted_df
