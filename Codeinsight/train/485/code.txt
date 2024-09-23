import pandas as pd

def test(df0, lst0, var0):
    return df0.assign(**{var0: df0[lst0].sum(axis=1)})
