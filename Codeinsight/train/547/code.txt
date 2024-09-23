def test(lst0):
    max_value = max(lst0)
    positions = []
    for i in range(len(lst0)):
        if lst0[i] == max_value:
            positions.append(i)
    return positions
