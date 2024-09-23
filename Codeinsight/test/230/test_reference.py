from operator import itemgetter 
def test(lst0):
    return sorted(lst0, key=itemgetter(1), reverse=True)