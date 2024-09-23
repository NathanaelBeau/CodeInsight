import pandas as pd

def test(df0, var0):
    return df0.sort_values(by=var0).reset_index(drop=True)
