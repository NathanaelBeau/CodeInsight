import pandas as pd
import numpy as np

def test(df0):
    return df0.apply(lambda x: x.fillna(x.mean()), axis=0)
