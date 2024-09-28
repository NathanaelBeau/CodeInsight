dict0 = {'a': 1, 'b': None, 'c': 3, 'd': None}
expected_output = {'b': 'updated', 'd': 'updated'}
assert test(dict0) ==expected_output, 'Test failed'