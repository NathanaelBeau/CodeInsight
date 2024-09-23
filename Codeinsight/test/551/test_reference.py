import pandas as pd

def test(df0):
    for col in df0.columns[1:]:
        df0[col] = df0[col].str.replace('$', '', regex=True).astype(float)
    return df0

