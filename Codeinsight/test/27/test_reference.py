import pandas as pd 

def test(df0, var0, date0, date1):
    return df0[(df0[var0] > date0) & (df0[var0] <= date1)]
