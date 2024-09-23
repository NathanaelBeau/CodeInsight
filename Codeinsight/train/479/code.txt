import pandas as pd
import numpy as np

def test(df0, var0, var1):
    df0[var0] = df0[var0].fillna(var1)
    return df0
