from bisect import bisect_left

def test(lst0, var0):
    pos = bisect_left(lst0, var0)
    if pos == 0:
        return lst0[0]
    if pos == len(lst0):
        return lst0[-1]
    before = lst0[pos - 1]
    after = lst0[pos]
    if after - var0 < var0 - before:
        return after
    else:
        return before

