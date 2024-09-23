import pandas as pd
import numpy as np

def test(df0):
    return np.mean(np.column_stack(np.nonzero(df0.to_numpy())))
