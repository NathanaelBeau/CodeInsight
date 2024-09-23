dict0 = {'a': [1.5, 2.5, 3.5], 'b': [4.5, 5.5, 6.5]}
expected_result =  {'a': 2.5, 'b': 5.5}
result = test(dict0)
assert result == expected_result, 'Test failed'