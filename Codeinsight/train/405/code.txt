import pandas as pd

import numpy as np

def test(df0: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(np.sort(df0.values)[:, ::-1], index=df0.index, columns=df0.columns)
