def test(df0):
    df0 = df0.sort_values(['year', 'month', 'day'])
    return df0.reset_index(drop=True)
