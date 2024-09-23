import pandas as pd
import datetime

def test(df0, timedelta0):
    df0.index = (pd.to_datetime(df0.index.astype(str)) + timedelta0).time
    return df0

