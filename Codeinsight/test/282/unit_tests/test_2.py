df0 = pd.DataFrame({'P': [7, 8, 9], 'Q': [10, 11, 12]})
var0 = 2
var1 = 1
var2 = 15
expected_result =  pd.DataFrame({'P': [7, 8, 9], 'Q': [10, 11, 15]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'