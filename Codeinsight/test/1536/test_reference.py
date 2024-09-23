def test(lst0):
    return max(lst0[i+1] - lst0[i] for i in range(len(lst0)-1))
