import pandas as pd
import numpy as np

def test(lst0):
    df = pd.DataFrame(lst0)
    u, c = np.unique(np.concatenate(df.categories.values), return_counts=True)
    result_series = pd.Series(c, u)
    return result_series.to_dict()
