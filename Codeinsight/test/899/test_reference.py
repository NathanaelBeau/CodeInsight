import pandas as pd


def test(df0, var0):
    return [group.reset_index(drop=True) for _, group in df0.groupby(var0)]
