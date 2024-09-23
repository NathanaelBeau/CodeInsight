import pandas as pd
def test(df0):
    return df0.sub(df0.mean(axis=1), axis=0)

