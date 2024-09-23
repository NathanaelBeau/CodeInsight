import numpy as np
import pandas as pd
def test(var0):
    return type(var0) in [list, np.ndarray, pd.Series]
