import pandas as pd

def test(df0):
    df0['sex'] = df0['sex'].replace({0: 'Female', 1: 'Male'})
    return df0

