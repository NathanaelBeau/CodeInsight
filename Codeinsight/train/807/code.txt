import pandas as pd
def test(df0, str0):
    return df0.drop([col for col in df0 if str0 in col], axis=1)
