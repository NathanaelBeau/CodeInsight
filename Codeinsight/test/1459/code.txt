import pandas as pd
import numpy as np

def test(df0, lst0):
    return df0[list(lst0)].max(axis=1)