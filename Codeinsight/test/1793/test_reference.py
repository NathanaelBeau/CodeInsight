from itertools import permutations

def test(lst0):
    return [''.join(p) for p in permutations(lst0, 2)]

