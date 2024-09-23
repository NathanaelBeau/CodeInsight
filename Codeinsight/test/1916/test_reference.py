import pandas as pd

def test(df0, var0, var1):
    df0[var1] = df0[var0].apply(lambda item: item.replace(' ', ''))
    return df0