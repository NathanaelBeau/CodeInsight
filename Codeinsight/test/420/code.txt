import pandas as pd
import numpy as np

def test(df0):
    return df0.replace(0, np.nan).dropna(axis=1, how="all")
