dict0 = {'a': 5, 'b': 2, 'c': 1}
results = [test(dict0) for _ in range(1000)]
assert results.count('a') > results.count('b') and results.count('b') > results.count('c'), 'Test failed'