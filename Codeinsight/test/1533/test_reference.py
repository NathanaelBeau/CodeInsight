def test(lst0):
    if len(lst0) <= 1:
        return [tuple(lst0)]
    permutations = []
    for i in range(len(lst0)):
        rest = lst0[:i] + lst0[i+1:]
        for p in test(rest):
            permutations.append(tuple([lst0[i]] + list(p)))
    return permutations
