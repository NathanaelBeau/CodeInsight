import pandas as pd

def test(df0, var0):
    return df0[pd.to_numeric(df0[var0], errors='coerce').isna()].reset_index(drop=True)
