dict0 = {'a': 0, 'b': 5, 'c': 5}
results = [test(dict0) for _ in range(1000)]
assert 'a' not in results, 'Test failed'