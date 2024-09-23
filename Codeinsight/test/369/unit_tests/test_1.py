var0 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
expected_result =  [('A', 2.0), ('B', 5.0)]
result = test(var0)
assert result == expected_result, 'Test failed'