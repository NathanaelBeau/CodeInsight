from itertools import permutations

def test(lst0):
    perm_pairs = set([tuple(zip(perm[::2], perm[1::2])) for perm in permutations(lst0)])
    return perm_pairs
