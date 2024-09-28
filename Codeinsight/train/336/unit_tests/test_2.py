# Test 3
df0 = pd.DataFrame({ 'Category': ['fruit', 'fruit', 'animal', 'fruit', 'animal'] })
var0 = 'Category'
var1 = 'animal'
expected_result =  [2, 4]
result = test(df0, var0, var1)
assert result == expected_result, 'Test failed'