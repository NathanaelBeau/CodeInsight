import pandas as pd

def test(df0):
    df0['B'] = df0['A']**2
    df0['C'] = df0['A']**3
    return df0

