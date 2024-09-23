import numpy as np

def test(df0):
    df0 = df0.iloc[np.random.permutation(len(df0))].reset_index(drop=True)
    return df0