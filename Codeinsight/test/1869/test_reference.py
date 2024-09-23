from functools import reduce

def test(lst0):
    return reduce(lambda x, elem: x + elem[0] + '\n', lst0, '').rstrip('\n')

