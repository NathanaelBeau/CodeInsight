from collections import OrderedDict
def test(str0):
    return " ".join(OrderedDict.fromkeys(str0))
