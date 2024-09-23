import pandas as pd

def test(df0, lst0, lst1):
    return df0.loc[lst0, lst1].agg('mean')
