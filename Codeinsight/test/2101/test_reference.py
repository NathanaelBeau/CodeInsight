from itertools import permutations

def test(lst0):
    perm_pairs = set()
    for perm in permutations(lst0):
        pairs = []
        for i in range(0, len(perm), 2):
            if i + 1 < len(perm):
                pairs.append((perm[i], perm[i + 1]))
            else:
                pairs.append((perm[i],))
        perm_pairs.add(tuple(pairs))
    return perm_pairs
