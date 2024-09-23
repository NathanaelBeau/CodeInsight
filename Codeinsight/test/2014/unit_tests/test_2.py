df0 = pd.DataFrame({'E': [1, 2, 3, 4, 5], 'F': [2, 4, 5, 8, 10]})
var0 = 'E'
var1 = 'F'
expected_result =   0.9901475429766742
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'