import pandas as pd

def test(df0):
    return pd.DataFrame({'count': df0.groupby(["Name", "City"]).size()}).reset_index()
