import pandas as pd
import numpy as np

def test(df0: pd.DataFrame):
    return df0.apply(lambda x: x.fillna(x.mean()), axis=0)

