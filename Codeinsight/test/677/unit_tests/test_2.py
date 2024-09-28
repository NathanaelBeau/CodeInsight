# Test 3
df0 = pd.DataFrame({ 'Category': ['fruit', 'animal', 'fruit'], 'Count': [5, 3, 2] })
lst0 = ['Category', 'Count']
expected_result =  pd.DataFrame({ 'Category': ['animal', 'fruit', 'fruit'], 'Count': [3, 2, 5] }, index=[1,2, 0])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'