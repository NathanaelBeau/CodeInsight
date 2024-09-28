df0 = pd.DataFrame({'A': [1, 2, 2, 3, 3, 3], 'B': [4, 5, 5, 6, 7, 7]})
var0 = 'A'
expected_result =  3
result = test(df0, var0)
assert result == expected_result, 'Test failed'