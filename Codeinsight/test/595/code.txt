import pandas as pd 

def test(df0, var0='dict'):
    return df0.to_dict(orient=var0)
