import numpy as np
import pandas as pd

def test(var0):
    return pd.isna(var0) or np.isnan(var0)
