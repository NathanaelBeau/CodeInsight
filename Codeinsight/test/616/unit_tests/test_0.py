df0 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
var0 = 'A'
lst0 = [1, 2]
expected_result =  pd.DataFrame({'A': [1, 2], 'B': [5, 6]})
result = test(df0, var0, lst0)
assert result.equals(expected_result), 'Test failed'