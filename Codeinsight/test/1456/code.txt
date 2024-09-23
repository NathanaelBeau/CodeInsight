from collections import OrderedDict

def test(var0):
    return ''.join(OrderedDict.fromkeys(var0).keys())