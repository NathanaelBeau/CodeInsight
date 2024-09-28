lst0 = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'d': 5}]
expected_output = {'a', 'b', 'c', 'd'}
assert test(lst0) == expected_output, 'Test failed'