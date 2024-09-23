import pandas as pd
def test(df0, lst0):
    reordered = lst0 + [c for c in df0.columns if c not in lst0]
    return df0[reordered]