from itertools import starmap
from operator import mul

def test(var0, var1):
    result = [sum(starmap(mul, zip(var0, col))) for col in zip(*var1)]
    return result
