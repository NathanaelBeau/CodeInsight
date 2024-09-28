import re

def test(df0, var0, var1):
    return df0[var0].apply(lambda x: bool(re.search(var1, x, re.I) if isinstance(x, str) else False)).any()
