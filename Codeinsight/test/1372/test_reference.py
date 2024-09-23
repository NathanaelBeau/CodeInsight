import pandas as pd

def test(df0):
    return df0['var0'].str.join('|').str.get_dummies()

