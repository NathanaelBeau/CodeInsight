import pandas as pd
import numpy as np

def test(df0):
    return df0.applymap(lambda x: np.nan if isinstance(x, str) and x.strip() == "" else x)
