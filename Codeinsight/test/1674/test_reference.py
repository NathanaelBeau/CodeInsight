import pandas as pd
import numpy as np

def test(df0, var0):
    return df0.query(f"{var0} != {var0}")
