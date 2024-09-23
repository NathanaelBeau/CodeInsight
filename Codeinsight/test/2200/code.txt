def test(lst0):
    return [(lst0[i], lst0[i+1]) for i in range(len(lst0)-1) if lst0[i] + lst0[i+1] > 10]
