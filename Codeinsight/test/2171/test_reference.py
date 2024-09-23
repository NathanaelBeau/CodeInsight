from collections import OrderedDict

def test(str0):
    
    unique_chars = list(OrderedDict.fromkeys(str0).keys())
    return unique_chars

