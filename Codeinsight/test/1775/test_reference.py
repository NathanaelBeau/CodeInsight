import pandas as pd
import numpy as np
def test(df0, var0, var1, var2):
    df0[var2] = np.where(df0[var0] == var1, var1, df0[var2])
    return df0
