import pandas as pd

def test(df0, func):
    return df0.applymap(func)
