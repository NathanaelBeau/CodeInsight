import pandas as pd
import numpy as np

def test(df0):
    nan_columns = df0.columns[df0.isna().all()]
    df_filtered = df0.drop(columns=nan_columns)
    return df_filtered
