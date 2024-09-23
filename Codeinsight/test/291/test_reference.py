import pandas as pd


def test(df0, var0, var1):
    df0['index'] = df0.index
    df0['index'] = df0['index'].replace(var0, var1)
    df0 = df0.set_index('index')
    return df0
