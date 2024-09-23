import numpy as np
import pandas as pd

def test(var0, str0):
    if str0 == "floor":
        return np.floor(var0)
    elif str0 == "ceiling":
        return np.ceil(var0)
    else:
        raise ValueError("Invalid operation. Choose 'floor' or 'ceiling'.")

