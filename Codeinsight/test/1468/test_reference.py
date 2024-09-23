import pandas as pd

def test(df0, var0, var1, var2, var3):
    df0[[var1, var2]] = df0[var0].str.extract(r'(.*)' + var3 + r'(.*)')
    return df0

