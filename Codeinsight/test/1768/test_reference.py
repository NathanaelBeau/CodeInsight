import pandas as pd
import numpy as np

def test(df0, col_name):
    return df0.dropna(subset=[col_name]).reset_index(drop=True)

