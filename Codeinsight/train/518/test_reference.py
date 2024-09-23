import pandas as pd

def test(df0):
    result = []
    for i, g in df0.groupby(["a", "b"]):
        result.append((i[0], g["c"].values.tolist()))
    return sorted(result)
