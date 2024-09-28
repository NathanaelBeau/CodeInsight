df0 = pd.DataFrame({'A': [1, 1, 1, 1], 'B': [4, 4, 4, 4]})
var0 = 'B'
expected_result =  1
result = test(df0, var0)
assert result == expected_result, 'Test failed'