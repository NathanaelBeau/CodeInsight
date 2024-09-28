df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
col0 = 'A'
var0 = 3
expected_result =  2
result = test(df0, col0, var0)
assert result == expected_result, 'Test failed'