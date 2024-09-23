# Test 2
df0 = pd.DataFrame({ 'X': [0, 50, 100], 'Y': [100, 50, 0] })
expected_result =  pd.DataFrame({ 'X': [0.0, 0.5, 1.0], 'Y': [1.0, 0.5, 0.0] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'