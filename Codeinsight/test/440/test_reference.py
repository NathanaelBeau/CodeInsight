import pandas as pd
import numpy as np

def test(df0, df1):
    return pd.DataFrame(df0.values - df1.values, index=df0.index, columns=df0.columns)
