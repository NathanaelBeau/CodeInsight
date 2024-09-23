import pandas as pd

def test(df0):
    df0['Date'] = pd.to_datetime(df0['Date'], format='%d-%m-%Y')
    return df0

