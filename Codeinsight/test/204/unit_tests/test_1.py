df0 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
var0 = 1
var1 = 'Y'
expected_result =  pd.DataFrame({'C': [7, 8, 9], 'Y': [10, 11, 12]})
result = test(df0.copy(), var0, var1)
assert result.equals(expected_result), 'Test failed'