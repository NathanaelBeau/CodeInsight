import pandas as pd 

def test(ser0, ser1):
    return pd.concat([ser0, ser1], axis=1)
