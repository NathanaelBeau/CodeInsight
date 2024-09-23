import pandas as pd

def test(df0):
    return (df0.T / df0.sum(axis=1)).T

