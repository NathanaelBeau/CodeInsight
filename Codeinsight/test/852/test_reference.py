import pandas as pd

def test(df0, var0, var1):
    grouped = df0.groupby(var0)[var1]
    df0[var0 + '_mean'] = grouped.transform('mean')
    df0[var0 + '_sum'] = grouped.transform('sum')
    return df0
