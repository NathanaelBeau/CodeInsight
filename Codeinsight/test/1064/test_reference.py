import pandas as pd

def test(df0, filename):
    df0.to_csv(filename, index=False)
    return f"DataFrame saved to {filename}"

