import pandas as pd
def test(df0):
    return df0.groupby(['A', 'B']).apply(lambda x: x[x['C'] == x['C'].max()]).reset_index(drop=True)

