import pandas as pd
import numpy as np

def test(df0):
    return df0[[col for col in df0.columns if not df0[col].isna().all()]]

