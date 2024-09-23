def test(lst0, var0):
    n = len(lst0)
    segment_length = n // var0
    remainder = n % var0
    result = []

    for i in range(var0):
        start = (segment_length + 1) * i if i < remainder else segment_length * i + remainder
        end = start + segment_length + (1 if i < remainder else 0)
        result.append(lst0[start:end])

    return result
