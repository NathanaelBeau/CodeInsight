# Test 3
df0 = pd.DataFrame({ 'Category': ['fruit', 'fruit', 'animal', 'animal', 'fruit'] })
var0 = 'Category'
expected_result =  pd.Series({'fruit': 3, 'animal': 2}, name='Category')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'