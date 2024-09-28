# Test 2
df0 = pd.DataFrame({'Category': ['X', 'Y', 'X', 'Y', 'Z', 'Z'], 'Item': ['apple', 'apple', 'banana', 'banana', 'apple', 'cherry']})
var0 = 'Category'
var1 = 'Item'
expected_result =  pd.Series([2, 2, 2], index=['X', 'Y', 'Z'], name='Item')
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'