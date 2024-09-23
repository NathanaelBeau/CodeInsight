def test(lst0):
    return [(lst0[i-1], lst0[i]) for i in range(1, len(lst0)) if lst0[i] == 9]
