import re

def test(df0, var0, var1):
    return df0[var0].str.contains(var1, case=False, na=False).any()
