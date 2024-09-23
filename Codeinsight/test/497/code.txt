import pandas as pd
import numpy as np
def test(df0):
    return df0.isnull().values.sum() > 0

