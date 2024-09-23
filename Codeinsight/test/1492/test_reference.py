import pandas as pd

def test(df0, var0):
    return df0[var0].str[1:-1].str.split(',', expand=True).astype(float)

