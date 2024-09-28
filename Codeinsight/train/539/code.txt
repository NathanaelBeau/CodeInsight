import pandas as pd 

def test(series0, method):
    if method == 'empty':
        return series.empty
    elif method == 'bool':
        return series.bool()
    elif method == 'item':
        return series.item()
    elif method == 'any':
        return series.any()
    elif method == 'all':
        return series.all()
    else:
        raise ValueError("Invalid method. Choose from 'empty', 'bool', 'item', 'any', or 'all'.")
