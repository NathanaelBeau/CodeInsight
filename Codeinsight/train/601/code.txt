import pandas as pd

def test(df0, var0, var1):

    df0[var1] = [item.replace(' ', '') for item in df0[var0]]
    return df0