import pandas as pd
def test(df0, var0, var1):
    return df0[df0[var0].str.contains(var1, na=False)]
