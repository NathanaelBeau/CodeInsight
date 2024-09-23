def test(lst0):
    result = []
    accumulator = 0
    for num in lst0:
        accumulator += num
        result.append(accumulator)
    return result
