import pandas as pd

def test(df0):
    return df0[df0.sum(axis=1) != 0]
