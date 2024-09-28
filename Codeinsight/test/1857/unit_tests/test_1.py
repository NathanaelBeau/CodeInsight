dict0 = {'name': 'John', 'age': 25, 'city': 'New York'}
expected_keys = ['name', 'age', 'city']
expected_values = ['John', 25, 'New York']
result_keys, result_values = test(dict0)
assert result_keys == expected_keys and result_values == expected_values, 'Test failed'