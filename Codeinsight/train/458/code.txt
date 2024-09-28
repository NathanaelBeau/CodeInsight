import pandas as pd

def test(df):
    df.columns = ['var1' if x=='var0' else x for x in df.columns]
    return df
