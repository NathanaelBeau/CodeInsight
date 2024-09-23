import pandas as pd
import numpy as np

def test(arr0, lst0, lst1):
    return pd.DataFrame(data=arr0, index=lst0, columns=lst1)

