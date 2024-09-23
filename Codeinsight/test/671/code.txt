import pandas as pd

def test(df0, var0, cond0, var1):
    df0[var0].replace(cond0, var1, inplace=True)
    return df0
