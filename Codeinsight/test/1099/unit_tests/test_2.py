df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
var0 = 'X'
expected_result =  pd.DataFrame({'Y': [40, 50, 60]})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'