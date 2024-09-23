import pandas as pd
import numpy as np
def test(df0):
    df0[['A', 'B']] *= df0['C'].values[:, np.newaxis]
    return df0[['A', 'B']]