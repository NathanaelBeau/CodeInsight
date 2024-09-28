dct0 = {'a': [5, 3], 'b': [4, 5], 'c': [6, 1]}
expected_result =  {'c': [6, 1], 'a': [5, 3], 'b': [4, 5]}
assert test(dct0) == expected_result, 'Test failed'