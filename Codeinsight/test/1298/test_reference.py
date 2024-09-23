from itertools import combinations
def test(lst0, var0):
    return [''.join(combination) for combination in combinations(lst0, var0)]
