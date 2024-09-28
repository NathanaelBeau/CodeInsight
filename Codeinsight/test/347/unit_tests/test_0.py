# Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3, 4] }, index=[1, 2, 2, 3])
expected_result =  pd.DataFrame({ 'A': [1, 2, 4] }, index=[1, 2, 3])
result = test(df0)
assert result.equals(expected_result), 'Test failed'