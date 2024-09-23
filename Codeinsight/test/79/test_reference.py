import pandas as pd

def test(df0):
    df0['name'] = df0['name'].str.replace(r"\(.*\)", "", regex=True)
    return df0

