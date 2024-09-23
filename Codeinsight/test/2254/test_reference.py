import numpy as np
import pandas as pd

def test(arr0):
    df = pd.DataFrame(arr0)
    sorted_df = df.sort_values(by=list(df.columns))
    return sorted_df.to_numpy()