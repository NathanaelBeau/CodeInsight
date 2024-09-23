import pandas as pd

def test(df0, var0):
    return df0[var0].str.split(',', expand=True).stack().reset_index(drop=True)
