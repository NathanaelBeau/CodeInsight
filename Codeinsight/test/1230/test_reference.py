import pandas as pd
def test(df0):
    return df0.apply(lambda row: ' '.join(map(str, row)), axis=1)
