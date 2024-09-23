import pandas as pd
import numpy as np

def test(columns_list0, n_rows0):
    return pd.DataFrame({col: [np.nan] * n_rows0 for col in columns_list0})

