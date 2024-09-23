import pandas as pd
import numpy as np

def test(df0):
    return df0[df0.isnull().any(axis=1)]
