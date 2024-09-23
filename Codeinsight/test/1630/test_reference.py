import pandas as pd
import numpy as np

def test(df0):
    return df0.dropna(axis=1, how='all')

