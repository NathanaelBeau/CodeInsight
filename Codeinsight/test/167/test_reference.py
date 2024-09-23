import pandas as pd

def test(df0):
    return df0.sort_values(by=['b', 'c'], ascending=[True, False])

