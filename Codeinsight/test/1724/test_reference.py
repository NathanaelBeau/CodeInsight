import pandas as pd

def test(df0, dict0):
    return pd.concat([
        df0,
        pd.DataFrame([dict0], columns=dict0.keys())]
    ).reset_index(drop=True)

df0 = pd.DataFrame(columns=('lib', 'qty1', 'qty2'))
dict0 = {'lib': 'A', 'qty1': 1, 'qty2': 2}

df0 = test(df0, dict0)

