def test(lst):
    return max(len(s) for sublist in lst for s in sublist)

