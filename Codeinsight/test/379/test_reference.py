from functools import reduce
import operator

def test(lst0):
    return reduce(operator.and_, lst0, True)

