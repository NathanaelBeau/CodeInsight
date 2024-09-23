import pandas as pd

def test(lst0):
    return lst0[lst0.duplicated()].tolist()
