import pandas as pd

def test(df0):
    return df0.apply(lambda x: x / x.sum(), axis=1)
