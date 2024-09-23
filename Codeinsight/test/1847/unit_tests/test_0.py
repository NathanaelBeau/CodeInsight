# Test 1
df0 = pd.DataFrame({ 'B': [1, 2, 3], 'A': [4, 5, 6], 'C': [7, 8, 9] })
expected_result =  pd.DataFrame({ 'A': [4, 5, 6], 'B': [1, 2, 3], 'C': [7, 8, 9] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'