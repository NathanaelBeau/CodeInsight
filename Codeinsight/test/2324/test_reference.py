import pandas as pd

from sklearn.preprocessing import MinMaxScaler

def test(df0):
    scaler = MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(df0), columns=df0.columns, index=df0.index)

