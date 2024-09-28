import pandas as pd

def test(df0, var0):
    return df0.loc[df0[var0].idxmax()]
