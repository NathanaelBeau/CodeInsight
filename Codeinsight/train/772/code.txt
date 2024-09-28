import pandas as pd
import numpy as np

def test(columns_list0, n_rows0):
    return pd.DataFrame({col: np.full(n_rows0, np.nan) for col in columns_list0})
