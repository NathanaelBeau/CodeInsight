

import pandas as pd

def test(df0):
    return df0.assign(B=df0['A']**2, C=df0['A']**3)

