var0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
var1 = pd.DataFrame({'X': [20, 30, 40], 'Y': [50, 60, 70]})
expected_result =  pd.DataFrame({'X': [10, 20, 30, 40], 'Y': [40, 50, 60, 70]})
result = test(var0, var1)
assert result.equals(expected_result), 'Test failed'