import pandas as pd

def test(df0, var0):
    df0['group_rank'] = df0.groupby(var0).cumcount() + 1
    return df0
