import pandas as pd

def test(df0, var0, var1):
    df0[var0 + '_mean'] = df0.groupby(var0)[var1].transform('mean')
    df0[var0 + '_sum'] = df0.groupby(var0)[var1].transform('sum')
    return df0
