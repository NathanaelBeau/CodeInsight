import pandas as pd
import numpy as np

def test(df0, method0='ffill'):
    df0.fillna(method=method0, inplace=True)
    return df0

