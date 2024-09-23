def test(lst0, var0):
    quotient, remainder = divmod(len(lst0), var0)
    result = []
    start = 0

    for i in range(var0):
        end = start + quotient + (1 if i < remainder else 0)
        result.append(lst0[start:end])
        start = end

    return result
