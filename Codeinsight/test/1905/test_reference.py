import pandas as pd
import numpy as np
def test(df0):
    df0['A'] = df0['A'] * df0['C']
    df0['B'] = df0['B'] * df0['C']
    return df0[['A', 'B']]

