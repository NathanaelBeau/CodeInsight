def test(df0):
    return df0.sort_values('count', ascending=False).groupby('Mt', as_index=False).first()