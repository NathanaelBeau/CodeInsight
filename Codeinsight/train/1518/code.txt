import pandas as pd 

def test(df0, lst0):
    return df0[~df0.index.isin(lst0)]
