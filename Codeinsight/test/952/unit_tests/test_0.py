dict0 = {'a': 'x', 'b': 'y', 'c': 'z'}
dict1 = {'x': 1, 'y': 2, 'z': 3}
expected_output = {'a': 1, 'b': 2, 'c': 3}
assert test(dict0, dict1) ==expected_output, 'Test failed'