import pandas as pd

def test(lst0):
    df = pd.DataFrame(lst0[1:], columns=lst0[0])
    return df