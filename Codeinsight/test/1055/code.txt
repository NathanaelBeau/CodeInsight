import pandas as pd

def test(df0, col0):
    df0['A'], df0['B'] = zip(*df0[col0])
    return df0.drop(col0, axis=1)
