df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6], 'B': [7, 8, 9, 10, 11, 12]})
var0= 2
expected_result =  pd.DataFrame({'A': [1, 3, 5], 'B': [7, 9, 11]})
result = test(df0, var0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'