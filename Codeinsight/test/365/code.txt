import pandas as pd


def test(df0, var0, var1):
    idx = list(df0.index)
    idx[idx.index(var0)] = var1
    df0.index = idx
    return df0