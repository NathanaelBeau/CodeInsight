import pandas as pd

def test(df0, var0):
    df0[var0] = df0[var0].apply(lambda x: x.date())
    return df0
