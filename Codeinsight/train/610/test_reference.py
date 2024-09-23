import pandas as pd
import numpy as np

def test(df0):
    return pd.Series([np.linalg.norm(row) for row in df0.values])
