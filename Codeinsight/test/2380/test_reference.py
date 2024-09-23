def test(lst0):
    max_diff = float('-inf')
    for i in range(len(lst0) - 1):
        diff = lst0[i+1] - lst0[i]
        if diff > max_diff:
            max_diff = diff
    return max_diff
