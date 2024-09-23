import pandas as pd
def test(df0, col0, var0):
    return df0[df0[col0] == var0].index[0]
