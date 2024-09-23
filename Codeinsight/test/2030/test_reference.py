from collections import defaultdict

def test(lst0):
    fq = defaultdict(list)
    for n, v in lst0:
        fq[n].append(v)
    return fq
