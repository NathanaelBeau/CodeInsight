dict0 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
expected_output = ['key1', 'key2', 'key3']
result = test(dict0)
assert result == expected_output, 'Test failed'