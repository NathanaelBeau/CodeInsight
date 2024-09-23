import pandas as pd

def test(df0):
    min_date = df0['Date'].min()
    max_date = df0['Date'].max()
    return pd.Series([min_date, max_date], index=['min', 'max'])
