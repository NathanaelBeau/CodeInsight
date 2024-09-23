import pandas as pd

def test(df0, dict0):
    return pd.concat([
        df0,
        pd.DataFrame([dict0], columns=dict0.keys())]
    ).reset_index(drop=True)

