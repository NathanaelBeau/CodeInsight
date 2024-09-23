import pandas as pd 
def test(df0, col0):
    return df0[col0].str.join('|').str.get_dummies()
