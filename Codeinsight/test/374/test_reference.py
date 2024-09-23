import operator

def test(lst0):
    lst0.sort(key=operator.attrgetter('resultType'))
    return lst0

