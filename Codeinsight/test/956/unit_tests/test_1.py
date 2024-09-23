# Test 3
df0 = pd.DataFrame({ 'P': [5, 10, 15], 'Q': [3, 6, 9] })
expected_result =  pd.DataFrame({ 'P': [0.0, 0.5, 1.0], 'Q': [0.0, 0.5, 1.0] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'