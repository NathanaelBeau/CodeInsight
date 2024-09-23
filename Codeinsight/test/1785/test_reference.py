import pandas as pd

def test(df):
    col_dict = {'var0': 'var1'}
    df.columns = [col_dict.get(x, x) for x in df.columns]
    return df