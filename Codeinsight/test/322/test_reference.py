import pandas as pd

def test(df0):
    return df0.apply(lambda row: row.idxmax(), axis=1)


