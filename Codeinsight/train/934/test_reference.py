def test(dict0):
    total = 0
    for value in dict0.values():
        if isinstance(value, dict):
            total += count(value)
        elif isinstance(value, list):
            total += len(value)
        else:
            total += 1
    return total
