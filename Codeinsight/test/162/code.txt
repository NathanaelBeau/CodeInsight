def test(df0, col_name):
    return df0.dropna(subset=[col_name])
