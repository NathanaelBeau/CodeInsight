# Test 1
df0 = pd.DataFrame({ 'A': [3, 1, 2], 'B': [1, 3, 2] })
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({ 'A': [1, 2, 3], 'B': [3, 2, 1] }, index=[1,2,0])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'