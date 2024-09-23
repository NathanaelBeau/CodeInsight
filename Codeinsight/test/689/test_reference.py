import pandas as pd
def test(df0, var0, var1):
    df0['helper'] = df0.groupby(var0).cumcount()
    result = df0.pivot(index='helper', columns=var0, values=var1)
    return result.reset_index(drop=True).drop(columns='helper', errors='ignore')

