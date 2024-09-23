from itertools import groupby
def test(var0):
    numbers = [''.join(g) for k, g in groupby(var0, str.isdigit) if k]
    chars = [''.join(g) for k, g in groupby(var0, str.isdigit) if not k]
    return numbers, chars
