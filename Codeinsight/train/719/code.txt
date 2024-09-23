import pandas as pd

def test(df0):
    return [df0.iloc[i].to_dict() for i in range(len(df0))]
