# Test 1
df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
var0 = 'dict'
expected_result =  {'A': {0: 1, 1: 2}, 'B': {0: 3, 1: 4}}
result = test(df0, var0)
assert result == expected_result, 'Test failed'