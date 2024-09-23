import pandas as pd

def test(df0):
    second_to_last_col = df0.columns[-2]
    last_col = df0.columns[-1]

    df0[second_to_last_col] = df0[second_to_last_col].replace({'\$': ''}, regex=True).astype(float)
    df0[last_col] = df0[last_col].replace({'\$': ''}, regex=True).astype(float)

    return df0
