import pandas as pd

def test(lst0):
    return pd.concat(lst0).reset_index(drop=True)
