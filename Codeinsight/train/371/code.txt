import pandas as pd

def test(df0):
    df0['x'] = df0.apply(lambda row: row['x'].lower() if isinstance(row['x'], str) and pd.isnull(row['x']) else row['x'], axis=1)
    return df0