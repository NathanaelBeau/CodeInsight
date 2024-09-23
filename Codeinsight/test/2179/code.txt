import pandas as pd

def test(lst0):
    header = lst0[0]
    data = lst0[1:]
    df = pd.DataFrame(data, columns=header)
    return df