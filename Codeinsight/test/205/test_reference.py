import pandas as pd
import numpy as np

def test(df0):
    numeric_cols = df0.select_dtypes(include=['number']).columns
    df0[numeric_cols] = df0[numeric_cols].fillna(df0[numeric_cols].mean())
    return df0


