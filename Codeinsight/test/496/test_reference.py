import numpy as np
import pandas as pd
from collections import OrderedDict

def test(var0, *var1):
    data_dict = OrderedDict(zip(var0, [pd.Series(arr) for arr in var1]))
    return pd.DataFrame(data_dict)

