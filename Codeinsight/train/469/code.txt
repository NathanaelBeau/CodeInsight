import pandas as pd
import numpy as np

def test(df0, var0, var1):
    return np.where(df0[var0] == var1)[0].tolist()
