df0 = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [1, 2, 3, 4, 5]})
var0 = 'X'
var1 = 'Y'
expected_result =  0.9999999999999999
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'