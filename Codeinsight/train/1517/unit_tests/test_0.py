d1 = {'key1': [1, 2, 3], 'key2': ['a', 'b', 'c']}
expected_output1 = [{'key1': 1, 'key2': 'a'}, {'key1': 2, 'key2': 'b'}, {'key1': 3, 'key2': 'c'}]
assert test(d1) == expected_output1, 'Test failed'