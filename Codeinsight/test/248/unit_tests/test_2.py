df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=[10, 20, 30])
var0 = 10
expected_result =  True
result = test(df0, var0)
assert result == expected_result, 'Test failed'