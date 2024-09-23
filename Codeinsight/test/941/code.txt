import pandas as pd

def test(lst0, lst1):
    return pd.DataFrame(list(zip(lst0, lst1)), columns=['List1', 'List2'])
