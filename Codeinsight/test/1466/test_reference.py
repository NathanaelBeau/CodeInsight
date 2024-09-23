import pandas as pd

def test(df0, var1, var0):
    grouped = df0.groupby(var1)
    return grouped.get_group(var0)

