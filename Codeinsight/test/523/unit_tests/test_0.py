# Test 1
df0 = pd.DataFrame({'Category': ['A', 'A', 'B', 'B'], 'Value': [1, 2, 3, 4]})
var0 = 'Category'
expected_result =  pd.DataFrame({'Value': [3, 7]}, index=['A', 'B'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'