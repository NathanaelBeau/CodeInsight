dict0 = {'a': [1, 2, 3], 'b': [4, 5, 6]}
dict1 = {'c': [7, 8, 9], 'd': [10, 11, 12]}
expected_output = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9], 'd': [10, 11, 12]}
assert test(dict0, dict1) ==expected_output, 'Test failed'