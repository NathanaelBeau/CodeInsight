from operator import itemgetter
import numpy as np

def test(arr0):
    return sorted(arr0, key=itemgetter(1))


