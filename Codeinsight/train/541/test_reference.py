import pandas as pd

def  test(df):
    df.rename(columns={'var0': 'var1'}, inplace=True)
    return df

