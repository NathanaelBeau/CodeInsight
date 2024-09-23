import pandas as pd

def test(lst0):
    factorized = pd.factorize(lst0)[0]
    return factorized


