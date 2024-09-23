def test(lst0):
    max_lengths = [max(len(str(x)) for x in line) for line in zip(*lst0)]
    return max_lengths

