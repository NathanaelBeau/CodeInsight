import pandas as pd

def test(df0, axis0):
    means = df0.mean(axis=axis0)

    if axis0 == 1:  # Row-wise normalization
        normalized_df = df0.sub(means, axis=0)
    else:  # Column-wise normalization
        normalized_df = df0.sub(means, axis=1)

    return normalized_df
