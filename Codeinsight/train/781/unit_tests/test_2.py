dict0 = {1: 'one', 2: 'two', 3: 'three'}
expected_keys = [1, 2, 3]
expected_values = ['one', 'two', 'three']
result_keys, result_values = test(dict0)
assert result_keys == expected_keys and result_values == expected_values, 'Test failed'