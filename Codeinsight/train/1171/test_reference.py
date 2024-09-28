def test(var0, dict0):
    count_success = lambda x: 1 if x[var0] else 0
    return sum(map(count_success, dict0))