lst0 = ['key1:value1', 'key2:value2', 'key3:value3']
expected_output = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
assert test(lst0) == expected_output, 'Test failed'