import pandas as pd


def test(df0, var0, var1):
    df0[var1] = df0.apply(lambda row: new_value if row[var0] > 2 else row[var1], axis=1)
    return df0
