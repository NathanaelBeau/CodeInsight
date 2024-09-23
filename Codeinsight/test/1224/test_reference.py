def test(lst0):
    return [lst0[i] + (lst0[i+1] if i+1 < len(lst0) else '') for i in range(0, len(lst0), 2)]
