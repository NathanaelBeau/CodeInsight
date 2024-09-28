import pandas as pd

def test(lst0, lst1):
    data = list(zip(*lst0))
    return pd.DataFrame(data, columns=lst1)
