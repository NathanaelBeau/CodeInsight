dict0 = {'a': 3, 'b': 2}
expected_result =  ['a', 'a', 'a', 'b', 'b']
result = test(dict0)
assert result == expected_result, 'Test failed'