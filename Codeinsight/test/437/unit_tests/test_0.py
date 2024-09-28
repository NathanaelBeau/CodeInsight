dict0 = {'a': 5, 'b': 3, 'c': 8}
dict1 = {'a': 2, 'c': 4}
expected_output = {'a': 3, 'b': 3, 'c': 4}
assert test(dict0, dict1) ==expected_output, 'Test failed'