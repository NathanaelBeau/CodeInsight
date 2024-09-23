import operator
def test(dict0):
    return sorted(dict0.items(), key=operator.itemgetter(1, 0))

