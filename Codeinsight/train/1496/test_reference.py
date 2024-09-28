def test(lst0):
    result = []
    for item in lst0:
        if isinstance(item, tuple):
            swapped = (item[1], item[0]) + item[2:]
            result.append(swapped)
        else:
            swapped = [item[1], item[0]] + item[2:]
            result.append(swapped)
    return result
