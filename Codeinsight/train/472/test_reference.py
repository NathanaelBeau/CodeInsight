def test(df0, var0, lst0):
    pattern = '|'.join(lst0)
    return df0[df0[var0].str.contains(pattern, case=False, na=False)]
