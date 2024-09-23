import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal

from sklearn.preprocessing import StandardScaler

def test(df0):
    scaler = StandardScaler()
    return pd.DataFrame(scaler.fit_transform(df0), columns=df0.columns)

