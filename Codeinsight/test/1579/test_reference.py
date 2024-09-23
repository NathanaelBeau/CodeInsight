import pandas as pd

def test(df0):
    return df0.applymap(lambda x: x.strip() if isinstance(x, str) else x)

