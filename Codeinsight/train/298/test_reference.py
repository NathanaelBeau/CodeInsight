import pandas as pd
import numpy as np

def test(var0, var1, var2, var3):
    return pd.DataFrame(np.random.randint(var0, var1, size=(var2, var3)), columns=list('ABCD'))

