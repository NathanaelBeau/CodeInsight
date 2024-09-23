import pandas as pd

def test(df0):
    return (df0 - df0.min()) / (df0.max() - df0.min())

