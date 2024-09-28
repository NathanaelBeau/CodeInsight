# Test 3
df0 = pd.DataFrame({'M': [10.5, np.nan, 12.5], 'N': [12.5, 13.5, np.nan]})
expected_result =  pd.DataFrame({'M': [10.5, 11.5, 12.5], 'N': [12.5, 13.5, 13]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'