import pandas as pd
def test(lst0):
    return pd.concat(lst0).groupby(level=0).mean()
