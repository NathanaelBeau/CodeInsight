import pandas as pd

def test(df0, var0):
    return df0[var0 ].drop_duplicates().sort_values().tolist()

