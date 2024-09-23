df0 = pd.DataFrame({'A': [1, 2, 2, 3, 3, 3, 4, 5]})
var0 = 'A'
expected_result =  3
result = test(df0, var0)
assert result == expected_result, 'Test failed'