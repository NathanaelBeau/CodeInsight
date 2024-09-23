import math
from operator import itemgetter

def test(lst0):
    return min(filter(lambda t: not math.isnan(t[1]), lst0), key=itemgetter(1))

