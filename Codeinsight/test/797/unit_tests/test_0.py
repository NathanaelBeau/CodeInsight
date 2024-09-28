var0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
var1 = pd.DataFrame({'A': [2, 3, 4], 'B': [5, 6, 7]})
expected_result =  pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 5, 6, 7]})
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'