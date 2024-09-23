import pandas as pd
import numpy as np

def test(df0):
    return df0.loc[:, df0.applymap(lambda x: not pd.isna(x)).any()]
