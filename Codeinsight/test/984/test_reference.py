import math

def test(lst0: list) -> float:
    return min(x[1] for x in lst0 if not math.isnan(x[1]))

