lst0 = ['key1', 'val1', 'key2', 'val2', 'key1', 'val3']
expected_output = {'key1': 'val3', 'key2': 'val2'}
assert test(lst0) ==expected_output, 'Test failed'