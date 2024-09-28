import pandas as pd
def test(df0, df1):
    return df0.assign(key=1).merge(df1.assign(key=1), on='key').drop(columns='key')

