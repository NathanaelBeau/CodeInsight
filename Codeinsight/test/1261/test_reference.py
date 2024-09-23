import pandas as pd

def test(var0, var1):
    data = {i: [0] * var0 for i in range(var1)}
    return pd.DataFrame.from_dict(data, orient='index').transpose()

