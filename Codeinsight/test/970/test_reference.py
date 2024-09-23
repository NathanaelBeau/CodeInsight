import pandas as pd
import numpy as np

def test(df0, var0, var1):
    ids = df0[var0].values
    vals = df0[var1].values

    m = np.isnan(vals)  
    grp_sums = np.bincount(ids, np.where(m, 0, vals))  
    avg_vals = grp_sums * (1.0 / np.maximum(np.bincount(ids, ~m), 1)) 

    vals[m] = avg_vals[ids[m]]  
    df0[var1] = vals
    return df0




