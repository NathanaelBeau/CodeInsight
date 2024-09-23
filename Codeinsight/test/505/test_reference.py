import itertools
def test(lst0):
    def recursive_combinations(lsts, idx=0, path=[]):
        if idx == len(lsts):
            yield tuple(path)
            return
        for item in lsts[idx]:
            yield from recursive_combinations(lsts, idx + 1, path + [item])

    results = []
    for result_tuple in recursive_combinations(lst0):
        results.append(result_tuple)
    return results

