import pandas as pd

def test(df0, var0, var1):
    group_sum = df0.groupby(var0)[var1].transform('sum')
    return df0[group_sum == 0]
