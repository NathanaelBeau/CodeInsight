import pandas as pd

def test(df0, str0, str1, str2):
    df0[[str1, str2]] = df0[str0].str.split(' ', n=1, expand=True)
    return df0

