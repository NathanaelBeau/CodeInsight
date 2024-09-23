import pandas as pd
def test(dataset0):
    return pd.DataFrame(data=dataset0.data, columns=dataset0.feature_names)
