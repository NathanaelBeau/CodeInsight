# Test 3
df0 = pd.DataFrame({'M': [7, 8, 9], 'N': [10, 11, 12]})
expected_result =  pd.DataFrame({'variable': ['M', 'M', 'M', 'N', 'N', 'N'], 'value': [7, 8, 9, 10, 11, 12]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'