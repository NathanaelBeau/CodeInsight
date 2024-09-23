import pandas as pd
import datetime

def test(df0, timedelta0):
    df0.index = [(datetime.datetime.combine(datetime.date.today(), t) + timedelta0).time() for t in df0.index]
    return df0

