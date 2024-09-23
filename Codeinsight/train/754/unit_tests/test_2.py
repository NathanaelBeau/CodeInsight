dict0 = {'a': [1, 2.5, 3], 'b': [4, 5.5, 6]}
expected_result =  {'a': 2.1666666666666665, 'b': 5.166666666666667}
result = test(dict0)
assert result == expected_result, 'Test failed'