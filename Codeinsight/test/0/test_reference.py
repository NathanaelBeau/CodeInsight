import pandas as pd
import numpy as np

def test(var0, var1, lst0, lst1):
    df = pd.DataFrame({var0: lst0, var1: lst1})
    tuples = list(zip(df[var0], df[var1]))
    unique_tuples, codes = np.unique(tuples, return_inverse=True, axis=0)
    return codes
