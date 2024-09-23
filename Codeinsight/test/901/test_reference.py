import pandas as pd
import numpy as np

def test(df0):
    return [col for col in df0.columns if df0[col].isnull().any()]

