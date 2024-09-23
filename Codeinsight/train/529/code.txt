import numpy as np
import pandas as pd

def test(arr0, arr1):
    return pd.Series(arr0).isin(arr1).any()
