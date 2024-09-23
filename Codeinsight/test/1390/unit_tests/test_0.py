df0 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'other_column': [10, 20, 30, 40]})
var0 = 'A'
var1 = 2
expected_result =  20
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'