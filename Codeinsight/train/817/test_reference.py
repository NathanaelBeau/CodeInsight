import pandas as pd
def test(df0, df1):
    df0['key'] = 1
    df1['key'] = 1
    result = pd.merge(df0, df1, on='key').drop(columns='key')
    return result


