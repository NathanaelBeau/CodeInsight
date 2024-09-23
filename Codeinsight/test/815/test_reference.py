import pandas as pd

def test(df0, col0, col1):
    df0['Time Difference'] = (df0[col1] - df0[col0]).dt.total_seconds() / 60
    df0['Hours'] = df0['Time Difference'] // 60
    df0['Minutes'] = df0['Time Difference'] % 60
    return df0[['Hours', 'Minutes']].astype({'Hours': 'int64', 'Minutes': 'int64'})


