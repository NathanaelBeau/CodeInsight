import pandas as pd

def test(df0):
    return df0.replace(to_replace="\[|\]", value="", regex=True)

