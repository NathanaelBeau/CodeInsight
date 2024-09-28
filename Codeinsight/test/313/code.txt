import pandas as pd
import numpy as np

def test(df0):
    return pd.to_numeric(df0.stack(), errors='coerce').unstack()
