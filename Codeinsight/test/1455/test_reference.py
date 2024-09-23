import pandas as pd

def test(df0, lst0, lst1):
    return df0[lst1].apply(lambda x: x.loc[lst0].mean())

