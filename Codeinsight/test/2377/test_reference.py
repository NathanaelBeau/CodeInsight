import pandas as pd
import numpy as np

def test(df0, var0):
    df0[var0] = df0.index
    return df0

