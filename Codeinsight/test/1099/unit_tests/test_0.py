df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
var0 = 'A'
expected_result =  pd.DataFrame({'B': [4, 5, 6]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'