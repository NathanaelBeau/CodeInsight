import pandas as pd

def test(df0):
    return df0.apply(lambda x: x.to_dict(), axis=1).tolist()

