import pandas as pd

def test(df0, var0, lst0):
    query_str = f"{var0} in @lst0"
    return df0.loc[df0[var0].isin(lst0)]
