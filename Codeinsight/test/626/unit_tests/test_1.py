df0 = pd.DataFrame({'D': [10, 11, 12], 'E': [13, 14, 15], 'F': [16, 17, 18]})
var0 = 10
expected_result2 = ['D']
result2 = test(df0, var0)
assert result2 == expected_result2, 'Test failed'