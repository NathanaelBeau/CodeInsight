import pandas as pd

def test(df0):
    return [row.to_dict() for _, row in df0.iterrows()]
