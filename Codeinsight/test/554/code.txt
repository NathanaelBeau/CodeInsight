def test(lst0):
    return [lst0[i] for i in range(len(lst0)) if i == 0 or lst0[i] != lst0[i-1]]
