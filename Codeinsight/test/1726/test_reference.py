import pandas as pd

def test(df0):
    return df0[df0.duplicated(keep=False)].shape[0]
