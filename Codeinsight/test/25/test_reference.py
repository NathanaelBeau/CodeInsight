import pandas as pd

def test(var0, lst0):
    if len(lst0) < 1:
        return []
    else:
        df = pd.DataFrame(lst0)
        return df[var0].tolist()