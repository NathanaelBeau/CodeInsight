dict0 = {'a': 1, 'b': 2, 'c': 3}
expected_keys = ['a', 'b', 'c']
expected_values = [1, 2, 3]
result_keys, result_values = test(dict0)
assert result_keys == expected_keys and result_values == expected_values, 'Test failed'