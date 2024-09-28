dict0 = {'a': 1, 'b': 2, 'c': 3}
dict1 = {'c': 3, 'b': 2, 'a': 1}
expected_output = True
assert test(dict0, dict1) == expected_output, 'Test failed'