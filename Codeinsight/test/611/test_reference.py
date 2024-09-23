import pandas as pd
def test(df0, operation):
    if operation == 'mean':
        return df0.mean().mean()
    elif operation == 'std':
        return df0.stack().std()
    else:
        raise ValueError("Invalid operation. Choose 'mean' or 'std'.")

