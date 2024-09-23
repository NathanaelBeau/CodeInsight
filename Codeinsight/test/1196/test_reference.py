import numpy as np

def test(lst0, var0=2):
    Q1 = np.percentile(lst0, 25)
    Q3 = np.percentile(lst0, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - (var0 * IQR)
    upper_bound = Q3 + (var0 * IQR)
    return lst0[(lst0 >= lower_bound) & (lst0 <= upper_bound)]
