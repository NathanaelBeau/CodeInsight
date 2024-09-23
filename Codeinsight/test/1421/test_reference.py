import numpy as np
import pandas as pd

def test(df0, str0='dummy', str1='returns'):
    return df0.groupby(str0).agg(Mean=(str1, np.mean),Sum=(str1, np.sum))

