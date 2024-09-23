import pandas as pd
def test(df0):
    mask = df0.ne(df0.shift()).any(axis=1)  
    return df0[mask].reset_index(drop=True)

