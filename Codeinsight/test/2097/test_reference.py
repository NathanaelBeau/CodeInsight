import pandas as pd
import numpy as np

def test(df0):
    mask = df0.notna().all(axis=1)
    return df0[mask]
