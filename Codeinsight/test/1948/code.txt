import numpy as np

def test(lst0, var0):
    top_var0_idx = np.argsort(lst0)[-var0:]
    top_var0_values = [lst0[i] for i in top_var0_idx]
    return top_var0_idx