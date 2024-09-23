from collections import OrderedDict

def test(str0: str) :
    Dict0 = OrderedDict.fromkeys(str0)
    str1 = " ".join(Dict0.keys())
    return str1

