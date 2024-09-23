import pandas as pd
import numpy as np

def test(df0):
    return pd.DataFrame(np.maximum(df0, 0), df0.index, df0.columns)

