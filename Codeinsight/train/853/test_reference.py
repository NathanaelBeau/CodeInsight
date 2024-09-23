import pandas as pd
import numpy as np
def test(df0, var0):
    df0['diff_column'] = df0[var0] - df0[var0].shift(1)
    return df0

