str0 = "{'key1': 1, 'key2': [1, 2, 3], 'key3': {'nested_key': 'value'}}"
expected_output = {'key1': 1, 'key2': [1, 2, 3], 'key3': {'nested_key': 'value'}}
assert test(str0) ==expected_output, 'Test failed'