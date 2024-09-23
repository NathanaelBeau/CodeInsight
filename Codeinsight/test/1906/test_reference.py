import pandas as pd

def test(df0, var0):
    df0[var0] = df0[var0].str.replace(r"\(.*\)", "", regex=True)
    return df0
