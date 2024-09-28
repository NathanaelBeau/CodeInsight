import pandas as pd
import numpy as np
def test(df0, var0, var1):
    return df0.groupby(var0)[var1].value_counts().unstack().fillna(0)
