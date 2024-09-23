# Test 3
df0 = pd.DataFrame({ 'Category': ['fruit', 'fruit', 'animal', 'animal'], 'Items': ['apple', 'banana', 'dog', 'cat'] })
var0 = 'Category'
var1 = 'Items'
expected_result =  pd.Series({ 'fruit': ['apple', 'banana'], 'animal': ['dog', 'cat'] }, name='Items')
result = test(df0, var0, var1)
assert result.sort_index().equals(expected_result.sort_index()), 'Test failed'