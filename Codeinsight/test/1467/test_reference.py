import pandas as pd
import numpy as np
def test(df0):
    return df0[["A", "B"]].multiply(df0["C"], axis="index")
