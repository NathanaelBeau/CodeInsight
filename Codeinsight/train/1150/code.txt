import pandas as pd

def test(df0, col0):    return df0.assign(**{col0: pd.factorize(df0[col0])[0]})
