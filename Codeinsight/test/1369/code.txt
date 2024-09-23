from sklearn.preprocessing import StandardScaler
import pandas as pd

def test(df0, lst0):
    scaler = StandardScaler()
    df0[lst0] = scaler.fit_transform(df0[lst0])
    return df0
