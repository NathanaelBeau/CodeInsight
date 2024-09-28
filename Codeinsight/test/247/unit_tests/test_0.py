str0 = "key1-value1, key2-value2, key3-value3"
expected_output = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
assert test(str0) ==expected_output, 'Test failed'