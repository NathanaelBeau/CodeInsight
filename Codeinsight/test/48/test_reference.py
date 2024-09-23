import pandas as pd
import numpy as np

def test(df0, var0, var1):
    mean_values = []
    for l in var1:
        mean_values.append(df0[var0].iloc[l].mean())

    mean_series = pd.Series(mean_values, index=var1)
    mean_matrix = pd.DataFrame(mean_series, columns=var0)

    return mean_matrix
