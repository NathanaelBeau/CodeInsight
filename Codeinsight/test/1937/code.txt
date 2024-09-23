import pandas as pd

def test(lst0, lst1):
    data = {lst1[i]: lst0[i] for i in range(len(lst1))}
    return pd.DataFrame(data)
