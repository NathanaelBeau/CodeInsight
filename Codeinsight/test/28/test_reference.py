import operator

def test(lst0, lst1):
    return list(map(operator.add, lst0, lst1))

