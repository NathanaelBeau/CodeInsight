dict0 = {'a': 1, 'b': 2}
dict1 = {'b': 3, 'c': 4}
expected_output = {'a': 1, 'b': 3, 'c': 4}
assert test(dict0, dict1) ==expected_output, 'Test failed'