import pandas as pd
def test(df0, col_name, var0):
    return df0.sample(frac=1).groupby(col_name).head(var0)

