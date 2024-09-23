import pandas as pd
import numpy as np

def test(df0):
    arr = df0.to_numpy()
    reshaped_arr = arr.reshape(arr.shape[0], -1, 3)
    mean_arr = np.mean(reshaped_arr, axis=2)
    new_df = pd.DataFrame(mean_arr)
    return new_df
