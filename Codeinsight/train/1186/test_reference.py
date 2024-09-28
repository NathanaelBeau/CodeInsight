import pandas as pd
import numpy as np

def test(df0, var0):
    return df0[df0[var0].isna()]
