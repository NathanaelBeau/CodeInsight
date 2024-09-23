import pandas as pd
import numpy as np


def test(df0, lst0):
    return df0[lst0].bfill(axis=1).iloc[:, 0]
