def test(var0, var1):
    result = []
    for col in zip(*var1):
        sum_result = 0
        for v, c in zip(var0, col):
            sum_result += v * c
        result.append(sum_result)
    return result