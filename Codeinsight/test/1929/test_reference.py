import pandas as pd
def test(df0):
    df0['col'] = df0['col'].map(int)
