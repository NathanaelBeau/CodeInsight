from bisect import bisect

def test(lst0):
    lst0.sort()
    i = bisect(lst0, 0)  # use `bisect_left` instead if you want zeros first
    return lst0[i:] + lst0[:i]

