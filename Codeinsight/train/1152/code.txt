import math

def test(lst0):
    return min(lst0, key=lambda x: float('inf') if math.isnan(x[1]) else x[1])
