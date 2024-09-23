import pandas as pd
import numpy as np

def test(df0):
    first_valid = df0.apply(lambda s: s.first_valid_index())
    last_valid = df0.apply(lambda s: s.last_valid_index())
    return first_valid, last_valid

