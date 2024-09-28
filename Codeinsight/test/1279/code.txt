import pandas as pd

def test(df0):
    return pd.DataFrame(df0.values, columns=df0.columns).reset_index(drop=True)