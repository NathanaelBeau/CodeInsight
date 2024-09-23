import pandas as pd
def test(df0):
    is_duplicate = (df0 == df0.shift()).all(axis=1)
    return df0[~is_duplicate].reset_index(drop=True)
