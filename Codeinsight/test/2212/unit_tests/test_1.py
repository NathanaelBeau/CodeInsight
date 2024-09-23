var0 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})
expected_result =  var0['X']
result = test(var0)
assert result.equals(expected_result), 'Test failed'