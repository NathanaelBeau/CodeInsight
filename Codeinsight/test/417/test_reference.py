def test(lst0):
    result = 0
    multiplier = 1
    for num in reversed(lst0):
        result += num * multiplier
        multiplier *= 10
    return result
