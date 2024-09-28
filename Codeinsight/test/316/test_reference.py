import pandas as pd
import numpy as np

def test(df0, str0):

    try:
        date_to_find = pd.Timestamp(str0)
        index = df0.index.get_loc(date_to_find)
        return index
    except KeyError:
        raise ValueError(f"Date '{str0}' not found in the DataFrame index.")