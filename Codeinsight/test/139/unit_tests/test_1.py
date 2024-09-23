# Test 2
df0 = pd.DataFrame({ 'Category': ['fruit', 'fruit', 'animal', 'animal'], 'Count': [5, 10, 2, 3] })
var0 = 'Category'
var1 = 'Count'
expected_result =  pd.DataFrame({ 'Category': ['animal', 'fruit'], 'Count': [3, 10] }, index=[3,1])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'