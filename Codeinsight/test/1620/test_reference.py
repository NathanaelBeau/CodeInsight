import pandas as pd
def test(df0, str0):
    return df0[[col for col in df0.columns if str0 not in col]]

