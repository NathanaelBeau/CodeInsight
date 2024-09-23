def test(df0):
    cols_to_drop = [col for col in df0.columns if not (df0[col] != 0).any()]
    return df0.drop(columns=cols_to_drop)