import pandas as pd

def test(df0, lst0):
    return df0.groupby(lst0).size().reset_index(name='var0')
