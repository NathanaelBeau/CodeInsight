import operator

def test(lst0, lst1):
    return sum(map(operator.mul, lst0, lst1))