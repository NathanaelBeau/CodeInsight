var0 = {'a': 1, 'b': 'banana', 'c': [1, 2, 3]}
expected_result =  [1, 'banana', [1, 2, 3]]
result = test(var0)
assert result == expected_result, 'Test failed'