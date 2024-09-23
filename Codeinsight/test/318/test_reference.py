import pandas as pd

def test(df0, str0, old_text, new_text):
    df0[str0] = df0[str0].str.replace(old_text, new_text)
    return df0

