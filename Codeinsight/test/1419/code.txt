import pandas as pd


def test(df0, var0, var1):
    df0.rename(index={var0: var1}, inplace=True)
    return df0