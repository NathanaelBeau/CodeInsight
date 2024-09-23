import operator

def test(lst0):
    lst0.sort(key=operator.itemgetter('weight', 'factor'))
    return lst0
