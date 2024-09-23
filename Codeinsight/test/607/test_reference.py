import pandas as pd
import numpy as np

def test(arr0):
    return arr0[~pd.isnull(arr0)]
