# Test 2
df0 = pd.DataFrame({'fruit': ['apple', np.nan, 'cherry'], 'color': [np.nan, 'yellow', 'red']})
expected_result =  pd.DataFrame({'fruit': ['apple', 'unknown', 'cherry'], 'color': [np.nan, 'yellow', 'red']})
result = test(df0, ['fruit'], 'unknown')
assert result.equals(expected_result), 'Test failed'