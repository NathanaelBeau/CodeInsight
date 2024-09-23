from itertools import product
def test(lst0):
    return [comb for comb in product(*lst0)]

