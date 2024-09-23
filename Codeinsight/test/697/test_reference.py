def test(df):
    return df.isnull().values.any()
