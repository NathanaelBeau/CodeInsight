import pandas as pd

def test(df0):
    df0['grade'] = pd.to_numeric(df0['grade']).astype(int)
    return df0

