from collections import OrderedDict
def test(var0):
    return OrderedDict(sorted(var0.items(), key=lambda x: x[1], reverse=True))
