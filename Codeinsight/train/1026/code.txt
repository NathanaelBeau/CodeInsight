import numpy as np
import pandas as pd 

def test(df0, var0):
    return df0.replace([np.inf, -np.inf], np.nan).dropna(subset=[var0], how="all")
