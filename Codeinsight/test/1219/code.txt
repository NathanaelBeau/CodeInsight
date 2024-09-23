import pandas as pd

def test(df0, df1):
    joined_df = df0.join(df1)
    return joined_df.dropna()
