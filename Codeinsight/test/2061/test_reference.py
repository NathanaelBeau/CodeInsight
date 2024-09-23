import pandas as pd
import numpy as np

def test(df: pd.DataFrame) -> pd.DataFrame:
    df.loc[df['A'] == 0, 'B'] = np.nan
    return df

