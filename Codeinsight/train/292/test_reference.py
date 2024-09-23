import pandas as pd
import numpy as np
def test(df0, str0, str1, var0):
    return pd.pivot_table(df0, index=str0, columns=str1, aggfunc=var0)

