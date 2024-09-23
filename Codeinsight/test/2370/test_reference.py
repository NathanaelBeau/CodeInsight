import pandas as pd
def test(df0, var0, var1):
    grouped = df0.groupby(var0)
    return grouped.get_group(var1)

