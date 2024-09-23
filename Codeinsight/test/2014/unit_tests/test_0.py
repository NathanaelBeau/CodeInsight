df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]})
var0 = 'A'
var1 = 'B'
expected_result =  -0.9999999999999999
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'