import pandas as pd
def test(df0, var0, var1):
    df0[[var1[0], var1[1]]] = df0[var0].str.split(pat=' ', n=1, expand=True)
    return df0

