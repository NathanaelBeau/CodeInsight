import pandas as pd

def test(df0, str0):
    return df0.drop([col for col in df0.columns if col.endswith(str0)], axis=1)