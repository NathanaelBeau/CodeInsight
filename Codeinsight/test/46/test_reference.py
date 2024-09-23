def test(df0):
    df0.drop(('col1', 'a'), axis=1, inplace=True)
    return df0

