def test(var0, var1):
    multiply_sum = lambda v, c: v * c
    result = list(map(lambda col: sum(map(multiply_sum, var0, col)), zip(*var1)))
    return result
