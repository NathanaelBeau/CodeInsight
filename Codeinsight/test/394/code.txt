import pandas as pd

def test(df0, df1, var0):
    return pd.concat([df0, df1]).sort_values(by=var0).reset_index(drop=True)
