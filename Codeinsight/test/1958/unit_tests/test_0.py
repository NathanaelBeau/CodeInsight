str0 = "key1-1, key2-2, key3-3"
expected_output = {'key1': 1, 'key2': 2, 'key3': 3}
assert test(str0) ==expected_output, 'Test failed'