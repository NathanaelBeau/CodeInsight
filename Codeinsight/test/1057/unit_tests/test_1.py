# Test 2
df0 = pd.DataFrame({'X': [5], 'Y': [6]})
expected_result =  pd.DataFrame({'variable': ['X', 'Y'], 'value': [5, 6]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'