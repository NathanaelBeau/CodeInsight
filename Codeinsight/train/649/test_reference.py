from itertools import permutations

def test(lst0):
    perm_pairs = set()
    for perm in permutations(lst0):
        pairs = [(perm[i], perm[i+1]) for i in range(0, len(perm), 2)]
        perm_pairs.add(tuple(pairs))
    return perm_pairs
