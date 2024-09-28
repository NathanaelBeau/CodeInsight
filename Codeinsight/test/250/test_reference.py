import numpy as np
def test(var0, var1, var2, var3):
    x = np.linspace(var0, var1-1, var1-var0)
    y = np.linspace(var2, var3-1, var3-var2)
    return np.meshgrid(x, y, indexing='ij')
