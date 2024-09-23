from operator import mul

def test(lst0, lst1):
    return sum(map(mul, lst0, lst1))
