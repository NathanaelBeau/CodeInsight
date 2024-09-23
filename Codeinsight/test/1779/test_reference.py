import pandas as pd 

def test(df0, df1):
    return df0[~df0.apply(tuple,1).isin(df1.apply(tuple,1))]
