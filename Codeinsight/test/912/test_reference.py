def test(lst0):
    max_value = max(lst0)
    positions = []
    index = -1
    while True:
        try:
            index = lst0.index(max_value, index + 1)
            positions.append(index)
        except ValueError:
            break
    return positions

