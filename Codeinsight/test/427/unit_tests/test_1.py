# Test 2
df0 = pd.DataFrame({ 'X': [1, 2, 2, 3, 3, 3], 'Y': [1, 1, 2, 2, 3, 3] })
lst0 = ['X', 'Y']
expected_result =  pd.DataFrame({ 'X': [1, 2, 3], 'Y': [2, 2, 2] }, index=[1, 2, 3])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'