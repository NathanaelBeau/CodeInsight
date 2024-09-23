import operator

def test(dict0):
    return dict(sorted(dict0.items(), key=operator.itemgetter(1), reverse=True))
