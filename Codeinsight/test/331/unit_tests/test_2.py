df0 = pd.DataFrame({'A': [1], 'B': [2]})
var0 = 5
expected_result =  pd.DataFrame({'A': [1], 'B': [2]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'