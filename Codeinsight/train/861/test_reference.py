import pandas as pd
import numpy as np

def test(df0, col0, val0, label_high, label_low):
    df0[col0] = np.where(df0['A'] > val0, label_high, label_low)
    return df0

