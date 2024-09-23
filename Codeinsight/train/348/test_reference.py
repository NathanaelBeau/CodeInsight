import pandas as pd
def test(df0):
    return df0.agg(' '.join, axis=1)